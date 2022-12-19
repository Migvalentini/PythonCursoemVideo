#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

for c in range(1,6):
    peso=float(input(f"Digite o peso da {c} pessoa: "))
    if c==1:
        maior,menor=peso,peso
    else:
        if peso>maior:
           maior=peso
        if peso<menor:
            menor=peso
        
print(f"O maior peso é {maior}kg e o menor peso é {menor}kg")