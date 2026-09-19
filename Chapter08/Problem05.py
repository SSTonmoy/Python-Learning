# Write a python function to print first n lines of the following pattern.
'''
***
**
*

n n-1 n-2 .... 1
n-(n-1)
'''


def stars(n):
    if n == 0:
        return
    print('*' * n)
    stars(n-1)


print(stars(15))
