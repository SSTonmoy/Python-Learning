# Write a python program to rename a file to “renamed_by_python.txt”.
'''with open('Chapter09/Apple.txt', 'r') as f:
    content01 = f.read()
with open('Chapter09/renamed_by_python.txt', 'w') as f:
    f.write(content01)
'''
import os

os.rename("Chapter09/Apple.txt", "Chapter09/renamed_by_python.txt")
