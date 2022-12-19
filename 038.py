#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

a = int(input("Digite o 1° número: "))
b = int(input("Digite o 2° número: "))

if a == b:
    print("Os dois números são iguais")
elif a > b:
    print("O primeiro valor é maior")
elif b > a:
    print("O segundo valor é maior")