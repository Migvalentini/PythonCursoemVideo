#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
# mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

ano = int(input("Digite o ano de nascimento: "))

idade = 2022 - ano

if idade < 9:
    categoria = "Mirim"
elif 9 <= idade < 14:
    categoria = "Júnior"
elif 14 <= idade < 19:
    categoria = "Infantil"
elif 19 <= idade < 25:
    categoria = "Sênior"
else: 
    categoria = "Master"
    
print(f"A idade do atleta em 2022 é de {idade} anos e sua categoria é {categoria}")