# Write a program to make a copy of a text file “this.txt”.
with open('Chapter09/this.txt', 'r') as f:
    content = f.read()
with open('Chapter09/thiscopy.txt', 'w') as f:
    f.write(content)
