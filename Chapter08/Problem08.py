# Write a python function to print multiplication table of a given number.
def multiplication_table(n):
    for i in range(1, 11):
        print(f'{n} X {i} = {i * n}')


n = int(input('Enter the number: '))
multiplication_table(n)
