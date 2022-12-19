#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

people = []
person = {}
woman = []
over_average = []
controller, sex = " ", " "
age_sum = 0

while controller != "N":
    name = str(input("Enter a name: "))
    sex = " "
    while sex not in "MmFf":
        sex = str(input("Enter a sex: ")).upper().strip()[0]
    age = float(input("Enter an age: "))
    person['name'] = name
    person['sex'] = sex
    person['age'] = age
    if sex == "F":
        woman.append(name)
    people.append(person.copy())
    age_sum += age
    controller = " "
    while controller not in "YyNn":
        controller = str(input("Do you want continue? ")).upper().strip()[0]
        
for p in people:
    print(p)
print(f"Was entered {len(people)} people")
print(f"The age average is {round(age_sum / len(people),2)} years")
print(f"The list of woman is {woman}")
print(f"The list of over age is: ", end="")
for p in people:
    if p['age'] >= age_sum / len(people):
        for k, v in p.items():
            print(f"{k} {v}", end=" ")
        print(" ")