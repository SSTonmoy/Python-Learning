# Write a program to create a dictionary of Bangla words with values as their Englis translation.
# Provide user with an option to look it up!
bangla = {
    'ma': 'mother',
    'baba': 'Father',
    'mama': 'uncle'
}
print('enter the word you want to know the meaning of')
print(bangla.keys())
word = input('> ')
print(bangla[word])
