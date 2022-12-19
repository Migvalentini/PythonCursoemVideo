#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
#e também indique o menor e o maior valor que estão na tupla.

from random import randint

tuple = tuple(randint(i + 1, 10) for i in range(5))
print(f"The orginal tuple is {tuple}")
print(f"The biggest number is {max(tuple)}")
print(f"The smallest number is {min(tuple)}")