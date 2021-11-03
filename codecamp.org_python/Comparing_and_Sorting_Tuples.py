d = {"a":10, "b":1, "c":22}
print(d.items()) #Prints out a list of the tuples of the dictionary d
print(sorted(d.items())) #prints out a sorted list of the dictionary d

d = {"c":22, "b":1, "a":10}
t = sorted(d.items()) #Stores the sorted items of the dictionary d in the variable t
print(t)

for k, v in sorted(d.items()): #for every key and value in the sorted items of the dictionary d 
    print(k, v) #print out the key and the value


c = {"c":22, "b":1, "a":10}
tmp = [] #creating a list. tmp = list() also works
for k, v in c.items(): #for key and value in the items of the dictionary c
    tmp.append( (v, k) ) #add the tuple of value and key in the list that we created. The value is stored first and then the key. Thats why its (v, k)
print(tmp) #printing that list with the tuples in it

tmp = sorted(tmp, reverse=True) #this means that the list is sorted and reversed, so that the highest value is printed out first and the lowest value is printed out last. Otherwise it would print out the lowest value first and the highest value
print(tmp)




fname = input("Enter a filepath here: ") #Entering a file
fhand = open(fname) #opening that file
counts = {} #making an empty dictionary called counts
for line in fhand: #for each line in the file that we opened
    words = line.split() #split every word in that line and store it in words
    for word in words: #and for every word in the words list
        counts[word] = counts.get(word, 0) + 1 #add the value 1 to the current key

lst = [] #making an empty list
for key, val in counts.items(): #for each key and value in the items of the dictionary counts
    newtup = (val, key) #store the value and the key in the variable newtup
    lst.append(newtup) #add that variable newtup with the keys and the values in it to the list that we created

#print("Unsorted list:\n",lst)

lst = sorted(lst, reverse=True) #Sorting the list from the highest value to the lowest value
#print("Sorted list:\n",lst)

for val, key in lst[:10]: #for every value and the key in the first 9 tuples in the list
    print(key, val) #first print out the key and then the value


c = {"a":10, "b":1, "c":22}
print(sorted([(v,k) for k,v in c.items()])) #Sorting the whole list of c.items() and printing it out with value, key