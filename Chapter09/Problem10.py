# Write a program to wipe out the content of a file using python
with open('Chapter09/Apple.txt', 'r') as f:
    content01 = f.read()
with open('Chapter09/Apple.txt', 'w') as f:
    f.write('')
