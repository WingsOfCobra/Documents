friends = ["Florian", "Lukas", "Manuel"]
for friend in friends: #For every friend in the friends list
    print("Happy new Year,", friend) #print a Happy New Year message
print("Done!") #And at the end print done

print(friends[1]) #print the Second Index String from the list "friends"

#Print a list with 5 numbers out
lotto = [5,72,62,14,13] 
print(lotto)

#Change the second number and print it out again
lotto[1] = 27
print (lotto)

#If you use the len() function on a String it tells you how much characters there are
greet = "Hello Bob!"
print(len(greet))

#But if you do it on lists it tells you how many items there are in. And btw it doesn't matter what types are in the lists
lotto = [5, 6.0, "joe mama", 97]
print(len(lotto))

#prints out a list of numbers from 0 to 4
print(range(4))

#printing out the range from a length of a list
friends = ["Florian", "Lukas", "Manuel"]
print(range(len(friends)))

#creating a for loop that prints out "Happy new year" for every friend in the friends list
for friend in friends:
    print("Happy new year,", friend)

#creating a for loop that prints out "Happy new year" for every Index-Number in the friends list
for i in range(len(friends)):
    friend = friends[i]
    print("\nHappy new year ", friend)