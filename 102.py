#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def factorial(number, show = False):
    fac = 1
    for n in range(1, number + 1):
        fac *= n
        if show == True:
            if n < number:
                print(n,"*", end = " ")
            else: 
                print(n, "=", end="")
    print(" ",fac)

number = int(input("Enter a number: "))
factorial(number, show=True)