a = [1, 2, 3]
b = [4, "Fünf", 6]
c = a + b

print(a)
print(c)
print(c[:5]) #print c up to but not including Index-Number 5

x = list()
#print(type(x))
#print(dir(x))

stuff = list() #makes an empty list and stores it into stuff
print("Before", stuff)
stuff.append("book") #adds a string to the empty list
stuff.append(21) #adds a integer to the list with the String
print("After", stuff)

some = [1,213,54,2,1,5,12]
print(9 in some)
print(9 not in some) #guten morgen

friends = ["Zeh", "Florian", "Anian"]
friends.sort() #sorts the friends list
print(friends) #prints the sorted list out
print(friends[2])

nums = [22,3,56,54,74,2,235,22]
print(len(nums)) #prints out how many numbers there are in the list
print(max(nums)) #prints the biggest number out of the list
print(min(nums)) #prints the smallest number out of the list
print(sum(nums)) #prints the sum of all the numbers in the list
print(sum(nums)/len(nums)) #prints out the sum of the numbers divided by the length of the numbers

#entering numbers and then calculating the average
#total = 0
#count = 0
#while True:
#    inp = input("Enter a number here: ")
#    if inp == "done":
#        break
#    try:
#        value = float(inp)
#    except:
#        print("Input is not a number!")
#        quit()
#    total = total + value
#    count = count + 1
#average = total / count
#print("Average:", average)

#entering numbers and then calculating the average with a while loop
numlist = list()
while True:
    inp = input("Enter a number here: ")
    if inp == "done":
        break
    try:
        value = float(inp)
    except:
        print("Input is not a number!")
        quit()
    numlist.append(value)

average = sum(numlist)/len(numlist)
print("Average:", average)
