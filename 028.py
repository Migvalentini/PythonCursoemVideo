from random import randint
from time import sleep

print("-=" * 20)
print("    Duvido você ganhar de mim KKKKKKK")
print("-=" * 20)

computador = randint(0,5)
usuario = int(input("Digite o número que você acha que eu escolhi: "))

print("PROCESSANDO...")
sleep(2)

if usuario == computador:
    print("Droga, você ganhou")
else:
    print(f"Hahaha, eu escolhi {computador} e você escolheu {usuario}")