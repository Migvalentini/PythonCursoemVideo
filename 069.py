#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 
 
over_age = 0
mens = 0
girls_less_20 = 0

while True:
    age = float(input("Enter you age: "))
    sex = " "
    while sex not in "MF":
        sex = str(input("Enter your sex [M/F]: ")).strip().upper()[0]
    if age > 18 :
        over_age+=1
    if sex == "M":
        mens+=1
    if sex == "F" and age < 20:
        girls_less_20 += 1
    controler = " "  
    while controler not in "CS":
        controler = str(input("Enter if you want continue or to stop [C/S]: ")).strip().upper()[0]
    if controler == "S":
        break
    
    
print(f"{over_age} people are over age!")
print(f"{mens} mens were registered!")
print(f"{girls_less_20} girls under 20 were registered!")