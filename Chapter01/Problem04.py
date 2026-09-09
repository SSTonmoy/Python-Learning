#Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
import os

# Specify the directory path (use '.' for the current directory)
path = '.'

try:
    # Get the list of all files and directories
    contents = os.listdir(path)
    
    print(f"Contents of '{path}':")
    for item in contents:
        print(item)
        
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")
