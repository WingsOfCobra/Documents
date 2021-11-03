import re

x = "My 2 favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x) #finds alle the digits in the x. [0-9]+ means one or more digits
print(y)

y = re.findall("[AEIOU]+" ,x)
print(y)

x = "From: Using the : character"
y = re.findall("^F.+:", x) #^F means the line has to start with a F. the ".+" means one or more characters. and the ":" means that the line has to end with a :. We could have got "From: " out of it, but because its one or more characters and there is a second ":" in the line, it takes the longer string. This is called Greede Matching.
print(y)

x = "From: Using the : character"
y = re.findall("^F.+?:", x) #We added the "?" so ".+?" means "One or more characters, but not greedy". This prefers the shorter string
print(y)

data = "From anian.sollinger@rsod.onmicrosoft.com Apr 3 08:38:12 2020"
y = re.findall("\S+@\S+", data) #means that there has to be at least one non-whitespace character before and after the at sign.
print(y)

data = "From anian.sollinger@rsod.onmicrosoft.com Apr 3 08:38:12 2020"
y = re.findall("^From (\S+@\S+)", data) #We want to find a line that Starts with "From" and then we want an at sign with at least one non-whitespace character. So we put the "\S+@\S" in parenthesis to exclude the "From" out of the String that we want to get out
print(y)