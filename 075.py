#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares

tuple = (float(input("Enter a number: ")), float(input("Enter a number: ")), float(input("Enter a number: ")), float(input("Enter a number: ")))
times_9 = 0
for position in tuple:
    if position == 9:
        times_9 += 1
position = 0
for position_tuple in tuple:
    position += 1
    if position_tuple == 3:
        position_3 = position
        break
pair = 0
for position in tuple:
    if position % 2 == 0:
        pair += 1
        
print(f"The number 9 appeared {times_9} times") #tuple.count(9)
print(f"The number 3 appears the first time in {position_3}° position") #tuple.index(3)
print(f"In the tuple there is {pair} pairs")