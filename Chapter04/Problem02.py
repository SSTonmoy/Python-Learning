# Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
student01 = input('Enter the mark of the first student: ')
marks.append(student01)
student02 = input('Enter the mark of the second student: ')
marks.append(student02)
student03 = input('Enter the mark of the third student: ')
marks.append(student03)
student04 = input('Enter the mark of the fourth student: ')
marks.append(student04)
student05 = input('Enter the mark of the fifth student: ')
marks.append(student05)
student06 = input('Enter the mark of the sixth student: ')
marks.append(student06)
marks.sort()

print(marks)
