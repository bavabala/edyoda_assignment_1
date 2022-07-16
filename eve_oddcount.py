 #count the number of even and odd numbers from a series of numbers.
num = (1, 2, 3, 4, 5, 6, 7, 8, 10)
odd = 0
even = 0

#Here,the for loop condition:
for i in num:
    if not i%2:
        even+=1
    else:
        odd+=1

#print the number of odd and even numbers:
print("Total even numbers: ",even)
print("Total odd numbers: ",odd)