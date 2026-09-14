# Write a program to find whether a given number is prime or no
num = int(input('Enter the number : '))
for i in range(2, num):
    if (num % i == 0):
        print(f'{num} is not prime')
        break
else:
    print(f'{num} is a prime numbers')
