# Write a program to calculate the factorial of a given number using for loop
num = int(input('Enter the number : '))
product = 1
for i in range(1, num+1):
    product = product * i

print(f'Factorial of {num} is {product}')
