import re

data = "From john.doe@loremipsum.onmicrosoft.com Apr 3 08:38:12 2020"
y = re.findall("^From .*@([^ ]*)", data) #The line has to start with "From", the ".*@" means that there can be any set of characters until an at sign appears. the "[^ ]*" means that the it stops searching at the next whitespace and the "*" means that there can be any set of characters. But only the things in the parenthesis are included when we print out y
print(y)

hand = open("mbox.txt")
numlist = list()
for line in hand: #for each line in that file
    line = line.rstrip() #remove whitespace on the right
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line) #searches for one or more digits or periods
    if len(stuff) != 1: #if the length of stuff is not 1
        continue #then continue, but if not then start over again
    num = float(stuff[0]) #the number in stuff is stored as a float
    numlist.append(num) #the float number is then added to the list we created
print("Maximum:", max(numlist))


x = "We just received $10.00 for cookies."
y = re.findall("\$[0-9.]+", x) #"\$" is a real Dollar sign.
print(y)