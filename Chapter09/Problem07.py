# Write a program to find out the line number where python is present from ques 6.
with open('Chapter09/finder.txt', 'r') as f:
    lines = f.readlines()
line = 1
for x in lines:
    if 'python' in x.lower():
        print(f'Found at line {line}')
        break
    line += 1
else:
    print('sorry')
