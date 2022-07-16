    #Reverse the string

#Here,we enter some string:
s =input('Enter string to reverse: ')
output = ''
i = len(s)-1

#Here,the loop condition:
while i >= 0:
    output = output+s[i]
    i = i - 1

#Here print the output:
print(output)


