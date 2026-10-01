# Write a program to mine a log file and find out whether it contains ‘pythonʼ.
with open('Chapter09/finder.txt', 'r') as f:
    content = f.read()
if 'Python' in content:
    print('Found')
else:
    print('sorry')
