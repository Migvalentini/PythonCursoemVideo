#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint

print("\033[34mJOGO: PEDRA, PAPEL E TESOURA\033[m")
print("\033[35mSuas opções:\033[m")
print("\033[36m[ 1 ] Pedra")
print("\033[33m[ 2 ] Papel")
print("\033[31m[ 3 ] Tesoiura\033[m")

u = int(input("Escolha sua Jogada: ")) #usuário

if u == 1 or u == 2 or u == 3:
    lista = ["Pedra","Papel","Tesoura"]
    c = randint(0, 2) #computador

    if u == 1:
        us = "Pedra"
    if u == 2:
        us = "Papel"
    if u == 3:
        us = "Tesoura"

    print(f"Eu escolhi {lista[c]} e você escolheu {us}")

    if (u == 1 and c == "Pedra") or (u == 2 and c == "Papel") or (u == 3 and c == "Tesoura"):
        print("\033[36mDeu empate!\033[m")
    elif (u == 1 and c == "Tesoura") or (u == 2 and c == "Pedra") or (u == 3 and c == "Papel"):
        print("\033[32mVocê Ganhou\033[m")
    else:
       print("\033[31mEu Ganhei\033[m")
else:
    print(print("\033[31mJogada Inválida\033[m"))