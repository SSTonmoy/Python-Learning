# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”.
# Write a program to detect these spams.
spam1 = input('Enter the word : ')
if (spam1 == 'Make a lot of money'):
    print('This is a spam word')
elif (spam1 == 'buy now'):
    print('This is a spam word')
elif (spam1 == 'subscribe this'):
    print('This is a spam word')
elif (spam1 == 'click this'):
    print('This is a spam word')
else:
    print('This is not a spam word')
