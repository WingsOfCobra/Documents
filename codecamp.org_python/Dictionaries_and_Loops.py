counts = dict()
print("Enter a line of text here: ") #Enter a line of text
line = input()
words = line.split() #splits every word in the line of text that we entered

print("Words: ", words) #Its gonna print every Word in a list of the line of text that we entered

print("Counting...")
for word in words: #for every word in the list of words
    counts[word] = counts.get(word, 0) + 1 #the counts of the word gets 1 bigger
print("Counts", counts)

counts = {"chuck"   :   1,  "fred"  :   42, "Jan"   :   100}
#           Key     :  Value, Key   :   Value,  Key :   Value

for key in counts: #for every key in the dictionary counts
    print(key, counts[key]) #print that key with the counts (value) of that key

age = {"chuck"   :   1,  "fred"  :   42, "Jan"   :   100}
#           Key     :  Value, Key   :   Value,  Key :   Value

for x in age: #for every x (key) in the dictionary "age"
    print(x, age[x]) #print the x (key) aswell as the value in the dictionary age, that is assigned to that specific key


jjj = {"Chuck" : 1, "ben" : 5, "simone" : 50, "Jan" : 185}

print(list(jjj)) #Prints the dictionary jjj as a list. But it only prints the keys, not the values that are assigned to the keys
print(jjj.keys()) #Prints only the keys in the dictionary jjj. Kind of the same as above, but differently
print(jjj.values()) #Prints only the values in the dictionary jjj. They come out in the same order as the keys

print(jjj.items()) #Gives you a list of the items that are in the dictionary

jjj = {"Chuck" : 1, "ben" : 5, "simone" : 50, "Jan" : 185}

for aaa,bbb in jjj.items(): #if you use items() then you have to use two variables. In my case aaa and bbb or else it will complain
    print(aaa,bbb) #the aaa variable is the key and the bbb var is the value

name = input("Enter a file: ")
handle = open(name)

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)