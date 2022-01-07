# Multi_Intent_Recognition

## english version below

Dies is die Einreichung von Jonathan Nöther für die SUSIS&James Coding Challenge(https://susiandjames.com/en/coding-challenge/). Es handelt es sich hierbei um eine API für Intent-Recognition. Das Skript für die API befindet sich im Ordner "API".
# Features im Überblick
- Erkennen von mehreren Intentionen in einem Text, auch wenn ein einzelner Teilsatz mehreren labels zugeordnet werden konnte
- Trainierte Domäne: Berichte und Notrufe zu Naturkatastrophen, Unfällen, etc.
- Benutzbarkeit in mehreren Sprachen(durch übersetzungs API)

# Domäne
Der disaster-responce Datensatz beinhaltet Berichte und Notrufe zu Katastrophen in verschieden Sprachen. Für das Training wurde allerdings die beinhaltete englische Übersetzung verwendet. Durch die beinhaltete übersetzungs-API sind allerdings Nutzereingaben in jeder Sprache möglich.
Beispiele aus dem Datensatz:
- Nachricht: Se grangou mwen grangou, se sak fe mwen te voye mesaj la
    - Deutsch : Ich bin hungrig, deswegen schreibe ich diese Nachricht
    - Label: Anfrage, Hilfe Benötigt, Essen

- Nachricht: Nou salye w nan non senye a! Nou se fanmi Jn jules ki konpoze de 15 manb ( 5g, 10f ) nap viv nan fe mikrdi nou bezwen ed ou paske kay nou kraze nou pedi
    - Deutsch: Wir sind eine Familie mit 15 Mitgliedern, 5 Männern und 10 Frauen, wir benötigen hilfe weil unser Haus eingestürzt ist
    - Label: Anfrage, Hilfe benötigt, Unterkunft, Gebäude

- Nachricht: Meanwhile, the death toll of soldiers in Tuesday's claymore mine explosion in the northern Jaffna peninsula increased to 12 after one soldier succumbed to his injuries in a hospital in Colombo.
    - Deutsch: Inzwischen hat sich die Zahl der Todesopfer unter Soldaten in der Claymore Explosion am Dienstag im Norden der Jaffna-Halbinsel auf 12 erhöht nachdem ein Soldat in einem Krankenhaus in Colombo an seinen Verletzungen verstarb.
    Label: Militär, Tod

- Nachricht: My thoughts and prayers go out to those who have been affected by the earthquake in Haiti
    - Deutsch: Meine Gedanken und Gebete gehen an die Opfer des Erdbebens in Haiti heraus.
    - Label: Wetter, Erdbeben

# Technische Beschreibung
- Dieses Projekt benutzt zur klassifizierung ein Neurales Netzwerk das mithilfe von Tensorflow trainiert wurde. Dieses besteht aus einem LSTM-layer sowie 2 Dense Layern. 
- Zur Übersetzung wird die Python library "Deep-translate" verwendet.  
- Um wie in der Aufgabenstellung gefordert einen Satz mit mehreren Teilsätzen getrenntvoneinander zu klassifizieren wird die eingabe gegebenenfalls in verschiedene Teile durch Wörter wie "und", "danach", etc. oder durch kommata in verschiedene eingaben getrennt.
- Wörter werden bevor sie in das NN eingegeben werden vektorisiert. Das hat den Vorteil, dass dadurch das zwei ähnliche wörte im (hier) 50-dimensionalen Raum nah zusammen liegen und dadurch ähnliche werte im Vektor haben. Das hat zur folge dass das Model auch gut mit Wörter welche nicht direkt im Trainingssatz waren funktioniert.
- Damit Label auch in einer beliebigen Sprache zurückgegeben werden können, lässt sich die gewollte Sprache als Query Parameter angeben(z.B. /resolve_intents_from_user_utterance/en gibt englische Label zurück). Wird keiner angegeben, werden die Label in deutscher Sprache zurück gegeben. Für die Spracherkennung der Eingabe wird dies nicht benötigt.

# Technische Evaluation
- Accuracy(Test Set): 95,80%
- Precision(Test Set): 96,35%
- Recall(Test Set): 98,72%
- F1(Test Set): 97,50%

Zusätzlich: Plots, z.B. Precision, Recall und F1 pro Label oder Confussion Matritzen im Model.ipynb Notebook(jupyter notebook benötigt)


## English
This is the submission of Jonathan Nöther for the SUSIS&James Coding Challenge(https://susiandjames.com/en/coding-challenge/). It is an API for Intent-Recognition. The script for the API is in the API-directory.

# Features
- Detection of multiple intentions of a sentence, even if a single sentence can be classified as multiple labels
- Domain: Reports and emergency calls for natural disasters, accidents, etc.
- Usability in multiple languages (by use of a translation API)

# Domain
The Disaster-Responce dataset consists of reports and emergency calls for disasters in multiple languages. For training, the provided english translation was used. By using the included translation-API inputs in every language are possible.
Examples from the dataset:
- Message: Se grangou mwen grangou, se sak fe mwen te voye mesaj la
    - Translation : I am hungry, Because of that, I am writing this message
    - Label: Request, Help Required, Food

- Message: Nou salye w nan non senye a! Nou se fanmi Jn jules ki konpoze de 15 manb ( 5g, 10f ) nap viv nan fe mikrdi nou bezwen ed ou paske kay nou kraze nou pedi
    - Translation: We are a family of 15, 5 men and 10 Women, we need help because our house collapsed
    - Label: Request, Help Required, Shelter, Building

- Message: Meanwhile, the death toll of soldiers in Tuesday's claymore mine explosion in the northern Jaffna peninsula increased to 12 after one soldier succumbed to his injuries in a hospital in Colombo.
    - Label: Military, Death


- Message: My thoughts and prayers go out to those who have been affected by the earthquake in Haiti
    - Label: Weather, Earthquake

# Technical Description
- This project uses a neural network for classification implemented with tensorflow. The architecture consists of a LSTM-layer and two dense layers
- For translation the Python libary "Deep-translate" is used
- Words are vectorized before they are used as input for the neural network. This results is two similar words are placed close together in the 50-dimensional space and have similar values in the resulting vector. Thus, the model performs well with words that are not part of the training set.
- To return classified labels in any language the required language can be used as a query parameter (e.g. /resolve_intents_from_user_utterance/en returns languages in english). By default, labels are returned in german.

# Technical Evaluation
- Accuracy(Test Set): 95,80%
- Precision(Test Set): 96,35%
- Recall(Test Set): 98,72%
- F1(Test Set): 97,50%

Additional plots, e.g. Precision, Recall und F1 for every label are accessible in the Model.iqynb notebook
