#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))

for c in range(primeiro_termo,primeiro_termo+(9)*razao,razao):
    print(c)