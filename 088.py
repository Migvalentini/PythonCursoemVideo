#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados 
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

num_games = int(input("Enter how much games do you want play: "))
list = []
games = []

for game in range(1, num_games+1):
    while len(list) != 6:    
        r = randint(1, 60)
        if r not in list:
            list.append(r)
    list.sort()
    games.append(list[:])
    list.clear()
 
for c in range(len(games)):
    print(f"Jogo {c+1}: {games[c]}")
    sleep(1)