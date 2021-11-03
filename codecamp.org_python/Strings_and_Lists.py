from os import startfile


abc = "With three words"

stuff = abc.split() #brakes the 3 words into a list with three items
print(stuff) 
print(len(stuff)) #prints the length of the list
print(stuff[1]) #prints the second item in the list

for w in stuff: #for every word(w) in the stuff list
    print(w) #print the word

line = "A lot        of spaces"
etc = line.split() #split without parameter looks for spaces and treats more than one spaces as 1 space
print(etc)

line = "first;second;third"
thing = line.split(";") #splits by semicolon
print(thing)
print("length:", len(thing))

line2 = "five-six-seven-eight"
thing = line2.split("-")
print(thing)
print("length:", len(thing))

fname = input("Enter your file path here: ") #Input for the filename
fhand = open(fname) #open function for the filename

for line in fhand: #for every line in the file handler
    line = line.rstrip() #remove the whitespace on the right side
    if not line.startswith("From "): #if the line doesn't start with "From "
        continue #then start the loop with the next line
    words = line.split() #but if it does, then split all the words in that line
    print(words[2]) #and print out the third word in the text file which is the day
    words = line.split()
    email = words[1]
    pieces = email.split("@")
    print(pieces)