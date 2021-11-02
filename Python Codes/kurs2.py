#input Funktionen und Variablen (1. November 2021)

#Lass uns einen Roboter bauen!


#Die Menu Variable in form eines Strings
menu = "Normaler Burger, Texas Burger, Chilli Burger, Cola, Sprite, Wasser"

#Begrüßung
print("Hallo, Willkommen zu Cobrascove Kaffee!")

#Es wird nach einem input gefragt, der automatisch in die Variable "name" gespeichert wird.
name = input("\nBitte geben sie hier ihren Namen ein: ")

#Diese variable wird dann in einer print Funktion verwendet, zusammen mit der menu Variable
print("\nWillkommen " + name + ".\nWas möchten sie bestellen?\nHier ist was wir für sie auf der Karte haben:\n\n" + menu)

#Es wird nach einem weiteren Input gefragt der direkt in die Variable "ordered_menu" gespeichert wird.
ordered_menu = input()


#Diese "ordered_menu" Variable wird dann in einer print Funktion benutzt und geschrieben.
print("\nGute Wahl " + name + ". Wir werden ihr(en) " + ordered_menu + " gleich für sie zubereiten.")
