searched_value = 69 #the value that we search for
equal = False #base boolean value
has_been_found = False #shows if the searched value has been found


print("Before", has_been_found)

for value in [2,3,6,54,2,4]:
    if value == searched_value: #If the value is equal to the searched value
        equal = True #then equal is set to True
        has_been_found = True #and has_been_found is set to True
    else: #if not
        equal = False #equal is set back to False
    print(value, equal) #Printing the value and if its equal during the loop

print("After", has_been_found)