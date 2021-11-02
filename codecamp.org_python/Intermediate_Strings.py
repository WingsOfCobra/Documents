s = "Monty Python"
fruit = "banana"


print(s[0:4]) #Printing the first 4 letters to the to the 4th Index-Number but the 4th Index-Number is not included

print(s[6:20]) #even if the variable s doesn't have that much Index-Numbers, Python won't give you a Traceback

print(s[:8]) #from beginning to 8
print(s[6:]) #from 6 to end
print(s[:]) #from beginning to end

if "Z" in fruit:
    print("Found it")

greet = "Hello Bob"

zap = greet.lower() #defining zap the same as greet but with all letters lowercase
print(zap)

stuff = "Hello World!"

#print(type(stuff)) #showing the type of the var stuff. In my case its a str (String)
#print(dir(stuff)) #printing out the methods that the var stuff contains.

fruit = "banana"

#b  a   n   a   n   a   The Word
#0  1   2   4   5   6   Index-Numbers

pos = fruit.find("na")  #searching for a Substring in the var fruit
print(pos)

greet = "Hello Bob"

nstr = greet.replace("Bob", "Jane") #replaces every "Bob" in the var greet with "Jane"
print(nstr)

nstr = greet.replace("o", "X") #replaces all lowercase O's with uppercase X's
print(nstr)

greet = "     Hello Bob   "

swstr = greet.lstrip() #the function "lstrip()" takes out all the whitespaces on the left side of the var. If there is nothing it doesn't harm it
print(swstr)

swstr = greet.rstrip() #This function takes out all whitespaces on the right side.
print(swstr)

swstr = greet.strip() #This function takes out all whitespaces
print(swstr)

line = "Please have a nice day"

pstr = line.startswith("Please") #This checks if a variable starts with the string given in the clauses
print(pstr)

pstr = line.startswith("p")
print(pstr)

data = "From anian.sollinger@rsod.onmicrosoft.com Apr 3 08:38:12 2020"

atpos = data.find("@") #Searches the first @ sign in the var data
print(atpos)

sppos = data.find(" ", atpos) #Searches the first Whitespace after the Index Position of the @ sign
print(sppos)

host = data[atpos + 1 : sppos] #Printing everything in between the position 21 (the Index-Number of the first @ sign + 1) and 41 but not including the 41 whitespace
print(host)