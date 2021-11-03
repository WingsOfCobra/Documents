purse = dict() #Creating an empty dictionary

purse["money"] = 12 #Throwing the twelve in the Dictionary with the label of money
purse["candy"] = 5 #Throwing the 5 in the Dictionary with the label of candy
purse["tissues"] = 6 #Throwing the 5 in the Dictionary with the label of tissues

print(purse) #Printing the whole Dictionary out
print(purse["candy"]) #Printing only the value with the label of candy (in my case it's 5)

purse["candy"] = purse["candy"] + 2
print(purse)
print(purse["candy"])

jjj = {"chuck":100, "Anian":57, "berry":5}
print(jjj)

ooo = {} #Is the same as "ooo = dict()" but its faster