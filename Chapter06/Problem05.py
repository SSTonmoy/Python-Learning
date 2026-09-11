# Write a program which finds out whether a given name is present in a list or not.
a = ['Hossain', 'Sabid', 'Atik']
n = input('Enter the name : ')
if (a[0] == n or a[1] == n or a[2] == n):
    print(f'{n} is on the list')
else:
    print(f'{n} is not on the list')
