#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

def counter(start, end, step):
    for num in range(start, end, step):
        print(num, end=' ')
    print()
        
counter(1, 10+1, 1)
counter(10, 0-1, -2)
counter(int(input("Enter the start: ")), int(input("Enter the end: ")), int(input("Enter the step: ")))