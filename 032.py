#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite o ano desejado: "))

if ano % 4 == 0:
    print(f"O ano {ano} é um ano bissexto")
else:
    print(f"O ano {ano} não é um ano bissexto")