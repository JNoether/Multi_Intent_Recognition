from hashlib import new
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from pathlib import Path
import numpy as np
import string
import re
import nltk
from deep_translator import GoogleTranslator
import uuid
from typing import Optional


#set working directory to path where script is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
print(os.getcwd())


##################################################################################
##  Data preprocessing                                                          ##
##################################################################################
# Load word vectorization method
import gensim.downloader
word2vec = gensim.downloader.load("glove-wiki-gigaword-50")

# maximal length of included words (also determines the amount of zero padding)
MAXLEN = 40

# Preprocessing functions
def remove_punctuation(text):
    return "".join([i for i in text if i not in string.punctuation])

def tokenitzation(text):
    return re.split("\W+", text)

def remove_empty(text):
    return [word for word in text if word]

stopwords = nltk.corpus.stopwords.words("english")
def remove_stopwords(text):
    return [word for word in text if word not in stopwords]

def vectorization(text):
    res = []
    for word in text:
        try:
            res.append(word2vec[word])
        except:
            res.append(np.zeros(50))
    # zero padding
    for _ in range(len(res), MAXLEN):
        res.append(np.zeros(50))
    return np.array(res)

def preprocess(text):
    # remove punctuation
    text = remove_punctuation(text)
    # remove uppercase
    text = text.lower()
    # tokenize
    text = tokenitzation(text)
    # remove empty strings
    text = remove_empty(text)
    #remove stopwords
    text = remove_stopwords(text)
    return text


#prepare data with one function(mostly for test and validation set, since I want to make plots 
# with the training set)
def prepare_data(text):
    text = preprocess(text)
    text = text[:40]
    text = vectorization(text)
    return np.array(text)


app = FastAPI()

class Message(BaseModel):
    message_uuid: str
    message: str


# load model
model = load_model(os.path.join(os.getcwd(), "Models", "Disaster-Responce"))
print(model)

labels = ["request", "offer", "aid_related","medical_help","medical_products","search_and_rescue","security","military","child_alone","water","food","shelter","clothing","money","missing_people","refugees","death"	
        ,"other_aid","infrastructure_related","transport","buildings","electricity","tools","hospitals","shops","aid_centers","other_infrastructure","weather_related","floods","storm","fire","earthquake","cold"	
        "other_weather", "direct_report"]


# object for translating
data_translator = GoogleTranslator(source="auto", target="en")

@app.post("/resolve_intents_from_user_utterance")
def resolve_intent(message: Message,label_language:Optional[str] = "de"):
    #tranlator for labels
    label_translator = GoogleTranslator(source= "auto", target = label_language)

    res = {}
    res["message_uuid"] = message.message_uuid
    res["intents"] = []

    #translate message into english
    message.message = data_translator.translate(message.message)

    messages = re.split(message.message, r"and|,|also|after|...")
    for message in messages:
        # preprocess data
        data = prepare_data(message)
        # predict
        prediction = model.predict(np.expand_dims(data, axis = 0))

        # create dictionary with the required information
        
        for i, label in enumerate(labels):
            if prediction[0][i] > 0.54:
                new_intent = {"intent":label_translator.translate(label), 
                            "confidence" : float(prediction[0][i]), "meta": {}}
                res["intents"].append(new_intent)
        return res