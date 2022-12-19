#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

person = {}

name = str(input("Enter a name: "))
year = int(input("Enter a year of birth: "))
work_card = int(input("Enter a work card: "))
age = datetime.now().year - year

person['Name'] = name
person['Year'] = year
person['Word_Card'] = work_card
person['Age'] = age

if work_card != 0:
    year_hire = int(input("Enter a year of hire: "))
    salary = float(input("Enter a salary: "))
    person['Year_Hire'] = year_hire
    person['Salary'] = salary
    retirement = age + ((year_hire +35)- datetime.now().year)
    person['Retirement'] = retirement
    
for k, v in person.items():
    print(f"The {k} is {v}")