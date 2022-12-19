#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
#Faça também um programa que importe esse módulo e use algumas dessas funções

from Módulos import coin

num = float(input("Enter a number: "))
percentage = float(input("Enter a percentage: "))
print(f"Increasing {percentage}%, the number is: {coin.increase(num, percentage)}")
print(f"Decreasing {percentage}%, the number is: {coin.decrease(num, percentage)}")
print(f"The double of {num} is: {coin.double(num)}")
print(f"The triple of {num} is: {coin.triple(num)}")