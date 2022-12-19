#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep

biggest = 0

gamers = {
    "Gamer 1": randint(1, 6),
    "Gamer 2": randint(1, 6),
    "Gamer 3": randint(1, 6),
    "Gamer 4": randint(1, 6),
}
ranking = {}
    
ranking = sorted(gamers.items(), key = itemgetter(1), reverse = True)

for pos, gamer in enumerate(ranking):
    print(f"{pos+1}° position: {gamer[0]} rolled {gamer[1]} on the die")
    sleep(0.5)