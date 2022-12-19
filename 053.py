#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input("Digite uma frase para ver se ela é palíndromo: ")).lower().replace(" ","")
inverso = frase[::-1]
if frase==inverso:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")