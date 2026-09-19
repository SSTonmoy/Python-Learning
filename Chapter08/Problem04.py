# Write a recursive function to calculate the sum of first n natural numbers.
'''def adder(sum):
    for x in range(1, num+1):
        sum += x
    return sum


num = int(input('How many number you want to add up to : '))
sum = 0

print(adder(sum))'''


def adder(n):
    if n == 1:
        return 1
    return adder(n-1)+n


print(adder(10))
