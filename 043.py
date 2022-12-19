# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua alturaem cenímetros: "))

IMC = peso / (altura/100 * altura/100)

print("Seu IMC é de",IMC)

if IMC < 18.5:
    print("Abaixo do Peso")
elif 18.5 <= IMC < 25:
    print("Peso Ideal")
elif 25 <= IMC < 30:
    print("Sobrepeso")
elif 30 <= IMC < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")