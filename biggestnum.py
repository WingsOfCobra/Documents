largest_so_far = -1 #Variable, basevalue = -1

print("Before", largest_so_far)
for the_num in [9, 38, 1, 93, 0, 29]: #starting the loop with variable the_num and some number
    if the_num < largest_so_far: #checking if the_num is bigger than largest_so_far
        largest_so_far = the_num #if true then largest_so_far is 
    print("\n", largest_so_far, the_num) #printing the largest number so far and the current number

print("\nAfter", largest_so_far) #print the largest number in the loop after the loop is done!