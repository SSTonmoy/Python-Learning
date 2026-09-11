# This program ask for my name and age then give me greetings
print('What is your name ??')
name = input()
print('How old are you ??')
age = int(input())
if age >= 18:
    print('You are an adult and you are responsible for yourself')
else:
    print('You are a minor and be respectful to the adults')

print(f'Hi {name}, hope you are doing well, and you are {age} years old')
# When combining multiple strings and variables using +, you must put a + between every part.
