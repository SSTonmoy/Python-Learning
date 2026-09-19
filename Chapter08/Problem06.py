# Write a python function which converts inches to cms.
def converter(inch):
    cm = inch * 2.54
    return cm


n = int(input("Enter the inch : "))
print(f'{converter(n)} cm')
