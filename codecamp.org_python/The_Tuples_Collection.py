(x,y) = (4, "Fred") #putting a tuple on the left-hand side of an assignment
print(y) #then printing one of the assignments
print(x)

(a,b) = (99,98)
print(a)
print(b)

u = dict()
u["Fred"] = 5 #This is a tuple
u["Jonas"] = 2.5 #This is also a tuple
for (k,v) in u.items(): #for every items in the dictionary (u) the key (k) and the value (v) are getting assigned
    print(k,v) #Then print out the key and the value

tups = u.items() #Stores ever tuple in a list and assigns it to tups
print(tups) #tups is being printed

#Comparing tuples together
print((0, 1, 2) < (5, 1 , 2)) #Only comapres the first ones
print((0, 1, 2000000) < (0, 5, 6)) #Compares the first ones but they are equal so it goes to the next one and checks and then it gives out True and moves to the next line of code, even though 2000000 is bigger than 6.