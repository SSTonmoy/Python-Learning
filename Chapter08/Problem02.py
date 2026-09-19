# Write a python program using function to convert Celsius to Fahrenheit.
def temp_converter(cel):
    far = ((cel * (9/5))+32)
    return far


cel = int(input('Enter the value of Celsius : '))
a = print(temp_converter(cel))
