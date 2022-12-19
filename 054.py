# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

maior,menor=0,0
for c in range(7):
    ano = int(input(f"Digite o ano de nascimento da {c+1}° pessoa: "))
    if date.today().year-ano>=18:
        maior+=1
    else:
        menor+=1
        
print(f"Há {maior} pessoas maiores que de idade e {menor} pessoas menores de idade")