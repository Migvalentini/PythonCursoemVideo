#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

from re import A


a = float(input("Digite o 1° número: "))
b = float(input("Digite o 2° número: "))
c = float(input("Digite o 3° número: "))

if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
    
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
    
print(f"O maior número é {maior}\nO menor número é {menor}")