#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from Módulos import coin108

num = float(input("Enter a number: "))
percentage = float(input("Enter a percentage: "))
print(f"Increasing {percentage:.0f}%, the number is: {coin108.coin(coin108.increase(num, percentage))}")
print(f"Decreasing {percentage:.0f}%, the number is: {coin108.coin(coin108.decrease(num, percentage))}")
print(f"The double of {num:.0f} is: {coin108.coin(coin108.double(num))}")
print(f"The triple of {num:.0f} is: {coin108.coin(coin108.triple(num))}")