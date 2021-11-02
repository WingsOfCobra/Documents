#input Funktionen und Variablen (1. November 2021)

#Lass uns einen Roboter bauen!

#Der Preis für alle Getränke in form eines Integers
price = 8

#Die Menu Variable in form eines Strings
menu = "Latte, Kaffee, Schwarzer Kaffee, Cola, Sprite, Wasser, Fanta"


print("Hallo, Willkommen zu Cobrascove Kaffee!")

#Es wird nach einem input gefragt, der automatisch in die Variable "name" gespeichert wird.
name = input("\nBitte geben sie hier ihren Namen ein: ")

#Diese variable wird dann in einer print Funktion verwendet, zusammen mit der menu Variable
print("\nWillkommen " + name + ".\nWas möchten sie bestellen?\nHier ist was wir für sie auf der Karte haben:\n\n" + menu)

ordered_menu = input()

quantity = input("\nGute Wahl, " + name + ". Wieviel Gläser von " + ordered_menu + " darf ich ihnen bringen?\n")

#Hier wird der gesamt preis zusammen gerechnet und ein string (quantity) in einen integer formatiert. Denn string + integer geht nicht
total = int(quantity) * price


print("\nVielen Dank für deine Bestellung.\nDu hast " + quantity + " mal " + ordered_menu + " bestellt.\nDeine gesamt Summe beträgt " + str(total) + "€.")


print("\nIhr(e) " + quantity + " bestellten " + ordered_menu + " werden ihnen hier gleich am Tisch serviert.")
