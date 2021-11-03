import re

#Before:
name = input("Enter a filepath here: ")
hand = open(name)
for line in hand:
    line = line.rstrip()
    if line.find("From: ") >= 0:
        print(line)

#After:
name = input("Enter a filepath here: ")
hand = open(name)
for line in hand:
    line = line.rstrip()
    if re.search("From: ", line):
        print(line)

#Using re.search() like startswith()

hand = open("mbox.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line): #the "^" character means that only "From:" at the beginning of the line matches. not in the middle or the end of the line.
        print(line)
