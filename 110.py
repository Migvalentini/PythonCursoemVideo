#Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

from Módulos import coin110

num = float(input("Enter a number: "))
percentage = float(input("Enter a percentage: "))

print(coin110.resume(num, percentage))