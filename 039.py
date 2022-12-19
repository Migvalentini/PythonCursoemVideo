#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou 
# se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input("Digite o ano de nascimento: "))

idade = 2022 - ano

print(f"Quem nasceu em {ano} tem {idade} anos em 2022")

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o seu alistamento")
    print(f"Seu alistamento será em {2022 + 18 - idade} ") 
if idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos")
    print(f"Seu alistamento foi em {2022 - (idade - 18)} ") 