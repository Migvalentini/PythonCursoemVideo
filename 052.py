#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input("Digite um número para saber se ele é primo: "))

divisor=0
for c in range(1,num+1):
    if num%c==0:
        divisor+=1
        print((f"\033[0;32m{c}\033[m"),end=" ")
    else:
         print((f"\033[0;31m{c}\033[m"),end=" ")
        
if divisor==2:
    print(f"\nO número {num} é primo")
else:
    print(f"\nO número {num} não é primo")