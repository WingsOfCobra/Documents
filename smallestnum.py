smallest = None #None is a constant value for nothing

print("Before", smallest)
for value in [9,12,52,2,5,887,42,6,5,23,345]: #start of the loop with numbers for value
    if smallest is None: #If the content of smallest is None. ("is" is greater than "=" because it also checks for the type of the variable not only for the content of the variable)
        smallest = value #then we take the first value of the loop to be the smallest
    if smallest > value: #if smallest is bigger than value
        smallest = value #then set smallest to be the current number
    print(smallest, value) #printing the smallest number and the current value

print("After", smallest)