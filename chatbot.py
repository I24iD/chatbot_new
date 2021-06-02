import random

zufallsantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]
reaktionen = {"hallo": "aber hallo",
		"geht": "Was verstehst Du darunter?",
		"schmeckt": "Ich habe keinen Geschmackssinn"}

print("Willkommen beim Chatbot (V1)")
print("Worüber wollen Sie sprechen?")
print("Zum Beenden geben Sie bye ein...")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
	nutzereingabe =""
	while nutzereingabe =="":
		nutzereingabe = input("Ihre Frage oder Antwort: ")
	nutzereingabe = nutzereingabe.lower()
	nutzerwoerter = nutzereingabe.split()

	intelligentAntworten = False
	for einzelwoerter in nutzerwoerter:
		if einzelwoerter in reaktionen:
			print(reaktionen[einzelwoerter])
			intelligentAntworten = True
            
	if not intelligentAntworten:
		print(random.choice(zufallsantworten))

print("einen schönen Tag!")