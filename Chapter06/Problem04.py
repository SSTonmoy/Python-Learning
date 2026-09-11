# Write a program to find whether a given username contains less than 10 characters or not.
username = input('Enter your user name : ')
print(len(username))
if (len(username) > 10):
    print('This username is bigger then 10 words')
else:
    print('The username is less then 10 words')
