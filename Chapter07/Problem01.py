# Write a program to print multiplication table of a given number using for loop
num = int(input('Enter the number you want the multiplication table for = >'))
i = 1
for i in range(1, 11):
    multiple = num*i
    print(f'{num} x {i} = {multiple}')
