#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

array = [[0,0,0],[0,0,0],[0,0,0]]

for line in range(3):
    for column in range(3):
        array[line][column] = int(input("Enter a number: "))
        
for line in range(3):
    for column in range(3):
        print(array[line][column], end=" ")
    print()