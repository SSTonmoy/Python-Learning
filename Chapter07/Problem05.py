# Write a program to find the sum of first n natural numbers using while loop.\
num = int(input('Enter the last number you want to sum up from 0 : '))
i = 1
sum = 0
while (i <= num):
    sum = sum + i
    i = i+1

print(sum)
