# Write a program to find out whether a student has passed or failed.
# If it requires a total of 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.
sub1 = int(input('Enter the marks of 1st subject out of 100 : '))
sub2 = int(input('Enter the marks of 2nd subject out of 100 : '))
sub3 = int(input('Enter the marks of 3rd subject out of 100 : '))
total = (sub1 + sub2 + sub3)/300
if (total < 40):
    print('You have failed the exam, Better luck next time')
else:
    print('You have passed the exam, Congratulation ')

if (sub1 < 33):
    print('You have failed 1st subject')
else:
    print('You have passed the 1st subject')

if (sub2 < 33):
    print('You have failed 2nd subject')
else:
    print('You have passed the 2nd subject')

if (sub3 < 33):
    print('You have failed 3rd subject')
else:
    print('You have passed the 3rd subject')
