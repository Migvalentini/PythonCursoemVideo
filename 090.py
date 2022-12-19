# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

student = {}

name = str(input("Enter a name: "))
average = float(input("Enter a average: "))

student["Name"] = name
student["Average"] = average
if student["Average"] >= 7:
    student["Situation"] = "Approved"
elif 5 <= student["Average"] < 7:
    student["Situation"] = "Recovery"
else:
    student["Situation"] = "Disapproved"

print("-="*20)
for k, v in student.items():
    print(f"{k} is equal to {v}")
print("-="*20)