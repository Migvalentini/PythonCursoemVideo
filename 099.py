#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores 
#e dizer qual deles é o maior.


def biggest(*num):
    cont = 0
    for number in num:
        cont += 1
        if number == num[0]:
            big = number
        if number > big:
            big = number
    print(f"Was entered {cont} numbers and the biggest number is {big}")

biggest (-8,-5,-9)
