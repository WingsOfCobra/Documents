word = "banana"

#b  a   n   a   n   a   - Word
#0  1   2   3   4   5   - Index-Numbers

#checking the second (Index-Number 1) number in the word banana
letter = word[1]
print(letter)

#checking the length of the variable "fruit"
print(len(word), "\n")

#checking the Index-Numbers of a word

index = 0
while index < len(word):
    letter = word[index]
    print(index, letter)
    index = index + 1

print("\n")

#showing every single letter in a word with a for loop without Index-Numbers

for letter in word:
    print(letter)