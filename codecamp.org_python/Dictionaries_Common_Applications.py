ccc = dict()
ccc["csev"] = 1
ccc["cwen"] = 1
print(ccc)
ccc["cwen"] = ccc["cwen"] + 1
print(ccc)

ccc = dict()
try:
    print(ccc["csev"]) #gives an error because "csev" is not in ccc
except:
    print("csev" in ccc) #"in" is a question, that gives back a boolean. "is csev in ccc?". Answer: False

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]

for name in names: #for every name in the list names
    if name not in counts: #if the name is not in the dictionary counts
        counts[name] = 1 #then set the value of the current name to 1
    else: #but if it is in there already
        counts[name] = counts[name] + 1 #then add 1 to the current value
print(counts)

#the same as the for loop above but here are 4 lines in one with the .get() function
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names: #for every name in the list names
    counts[name] = counts.get(name, 0) + 1 #the dictionary counts sets a default value of 0 for the current name, but if there already is a value for that name then it adds 1 to it
print(counts)