# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer():
    company = 'Microsoft'

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


Tonmoy = Programmer('Tonmoy', 20, 120000)
print(f'Name = {Tonmoy.name}\nAge = {Tonmoy.age}\nSalary = {Tonmoy.salary}\n')
Hoaasin = Programmer('Hossain', 22, 150000)
print(f'Name = {Hoaasin.name}\nAge = {Hoaasin.age}\nSalary = {Hoaasin.salary}\n')
Atik = Programmer('Atik', 25, 1000)
print(f'Name = {Atik.name}\nAge = {Atik.age}\nSalary = {Atik.salary}\n')
Sabid = Programmer('Sabid', 69, 1200000)
print(f'Name = {Sabid.name}\nAge = {Sabid.age}\nSalary = {Sabid.salary}\n')
