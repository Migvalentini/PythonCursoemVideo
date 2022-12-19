# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input("Type how much terms do you want: "))
t1 = 1
t2 = 2
cont = 2
while cont <= n:
    tn = t1 + t2
    t2 = tn 
    cont+=1
    
print(f"The {n}° term of Fibonacci is {tn}")