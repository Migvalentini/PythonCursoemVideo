#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("\Digite a distância da viagem em km: "))

if km < 200:
    preco = 0.5 * km
else:
    preco = 0.45 * km
    
print(f"Você está prestes a viagem {km} quilômetros")
print(f"Para isso, você irá pagar R${preco}")