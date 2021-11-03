#xfile = open(r"C:\Users\anian\OneDrive\Dokumente\GitHub\Documents\codecamp.org python\mbox.txt")

#for cheese in xfile: #cheese is just a name for "each line" so "for each line in the xfile" and then with the print function it prints it all out
#    print(cheese)


#fhand = open(r"C:\Users\anian\OneDrive\Dokumente\GitHub\Documents\codecamp.org python\mbox.txt")
#count = 0

#for line in fhand: #for each line in fhand
#    count = count + 1 #count gets 1 bigger
#print("Line count:", count)

#fhand = open(r"C:\Users\anian\OneDrive\Dokumente\GitHub\Documents\codecamp.org python\mbox.txt")

#inp = fhand.read() #reads the fhand file
#print(len(inp)) #shows the number of characters in the inp file

#print(inp[:20]) #Prints the Index-Numbers from 0-19 because the 20 is not included

#Searching for lines that have a prefix with "From:" and then prints the lines (with linebreaks)
#fhand = open(r"C:\Users\anian\OneDrive\Dokumente\GitHub\Documents\codecamp.org python\mbox.txt")
#for line in fhand:
#    if line.startswith("From:"):
#        print(line)

#Searching for lines that have a prefix with "From:" and then prints the lines (without linebreaks)
#fhand = open(r"C:\Users\anian\OneDrive\Dokumente\GitHub\Documents\codecamp.org python\mbox.txt")
#for line in fhand:
#    line = line.rstrip()
#    if line.startswith("From:"):
#        print(line)

#Looking for a line prefix with the if not and continue statement
#fhand = open(r"C:\Users\anian\OneDrive\Dokumente\GitHub\Documents\codecamp.org python\mbox.txt")
#for line in fhand:
#   line = line.rstrip()
#    if not line.startswith("From:"): #if the line does not contain the prefix "From:"
#        continue #then continue with the for loop. But if it has a line with the prefix "From:"
#    print(line) #then print it


#Looking for a string in a line
#fhand = open(r"C:\Users\anian\OneDrive\Dokumente\GitHub\Documents\codecamp.org python\mbox.txt")
#for line in fhand:
#   line = line.rstrip() #removing the linebreak
#    if not "@uct.ac.za" in line: #if the string "@uct.ac.za" is not in the line
#        continue #then continue. but if it is
#    print(line) #then print the line


fname = input("Enter the File name: ") #asks for a file to input
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0

for line in fhand: #for each line in fhand
    if line.startswith("Subject:"): #if the line starts with "Subject:" then
        count = count + 1 #add 1 to the count
print("There were", count, "subject lines in", fname) #print the result out