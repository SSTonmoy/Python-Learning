# Write a program using functions to find greatest of three numbers.
def greatest(x, y, z):
    if (x > y and x > z):
        return (x)
    elif (y > x and y > z):
        return (y)
    elif (z > y and z > x):
        return (z)


x = int(input('Enter the 1st number : '))
y = int(input('Enter the 2nd number : '))
z = int(input('Enter the 3rd number : '))
print(greatest(x, y, z))
