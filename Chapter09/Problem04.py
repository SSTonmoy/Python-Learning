# A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.
word = 'Donkey'

with open('Chapter09/Donkey.txt', 'r') as f:
    content = f.read()

new_content = content.replace(word, '#####')

with open('Chapter09/Donkey.txt', 'w') as f:
    f.write(new_content)
