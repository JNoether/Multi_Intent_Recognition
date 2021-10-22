# Multi_Intent_Recognition

Dies is die Einreichung von Jonathan Nöther für die SUSIS&James Coding Challenge(https://susiandjames.com/en/coding-challenge/).
# Features im Überblick
- Erkennen von mehreren Intentionen in einem Text, auch wenn ein einzelner Teilsatz mehreren labels zugeordnet werden konnte
- Trainierte Domäne: Berichte und Notrufe zu Naturkatastrophen, Unfällen, etc.
- Benutzbarkeit in mehreren Sprachen(durch übersetzungs API)

# Domäne
Der disaster-responce Datensatz beinhaltet Berichte und Notrufe zu Katastrophen in verschieden Sprachen. Für das training wurde allerdings die beinhaltete englische übersetzung verwendet. Durch die beinhaltete übersetzungs-API sind allerding Nutzereingaben in jeder Sprache möglich.
Beispiele aus dem Datensatz:
- Nachricht: Se grangou mwen grangou, se sak fe mwen te voye mesaj la
    - Deutsch : Ich bin hungrig, deswegen schreibe ich diese Nachricht
    - Label: Anfrage, Hilfe Benötigt, Essen

- Nachricht: Nou salye w nan non senye a! Nou se fanmi Jn jules ki konpoze de 15 manb ( 5g, 10f ) nap viv nan fe mikrdi nou bezwen ed ou paske kay nou kraze nou pedi
    - Deutsch: Wir sind eine Familie mit 15 Mitgliedern, 5 Männern und 10 Frauen, wir benötigen hilfe weil unser Haus eingestürzt ist
    - Label: Anfrage, Hilfe benötigt, Unterkunft, Gebäude

- Nachricht: Meanwhile, the death toll of soldiers in Tuesday's claymore mine explosion in the northern Jaffna peninsula increased to 12 after one soldier succumbed to his injuries in a hospital in Colombo.
    - Deutsch: Inzwischen hat sich die Zahl der Todesopfer unter Soldaten in der Claymore explusion am Dienstag im Norden der Jaffna-Halbinsel auf 12 erhöht nachdem ein Soldat in einem Krankenhaus in Colombo an seinen Verletzungen verstarb.
    Label: Militär, Tod

- Nachricht: My thoughts and prayers go out to those who have been affected by the earthquake in Haiti
    - Deutsch: Meine Gedanken und Gebete gehen an die Opfer des Erdbebens in Haiti heraus.
    - Label: Wetter, Erdbeben

# Technische Beschreibung
- Dieses Projekt benutzt zur klassifizierung ein Neurales Netzwerk das mithilfe von Tensorflow trainiert wurde. Dieses besteht aus einem LSTM-layer sowie 2 Dense Layern. 
- Zur Übersetzung wird die Python library "Deep-translate" verwendet.  
- Um wie in der Aufgabenstellung gefordert einen Satz mit mehreren Teilsätzen getrenntvoneinander zu klassifizieren wird die eingabe gegebenenfalls in verschiedene Teile durch Wörter wie "und", "danach", etc. oder durch kommata in verschiedene eingaben getrennt.
- Wörter werden bevor sie in das NN eingegeben werden vektorisiert. Das hat den Vorteil, dass dadurch das zwei ähnliche wörte im (hier) 50-dimensionalen Raum nah zusammen liegen und dadurch ähnliche werte im vektor haben. Das hat zur folge dass das Model auch gut mit Wörter welche nicht direkt im Trainingssatz waren funktioniert.
- Damit Label auch in einer beliebigen Sprache zurückgegeben werden können, lässt sich die gewollte Sprache als Query Parameter angeben(z.B. /resolve_intents_from_user_utterance/en gibt englische Label zurück). Wird keiner angegeben, werden die Label in deutscher Sprache zurück gegeben.

# Technische Evaluation
- Accuracy(Test Set): 95,80%
- Precision(Test Set): 96,35%
- Recall(Test Set): 98,72%
- F1(Test Set): 97,50%

Zusätzlich: Plots, z.B. Precision, Recall und F1 pro Label oder Confussion Matritzen im Model.ipynb Notebook(jupyter notebook benötigt)