#  Write a program to find out whether a file is identical
# and matches the content of another file.
with open('Chapter09/this.txt', 'r') as f:
    content01 = f.read()
with open('Chapter09/thiscopy.txt', 'r') as f:
    content02 = f.read()

if (content01 == content02):
    print('Matches')
else:
    print('Did not match')
