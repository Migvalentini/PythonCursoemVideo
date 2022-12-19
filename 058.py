#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
from random import randint

computador=randint(0,10)
print(computador)
print("\033[0;34m====SEJA BEM VINDO====\033[m")
print("\033[0;36mEu sou o computador e escolhi um número de 0 a 10\033[m")
jogador=int(input("Tente adivinhar qual número eu escolhi: "))
tentativas=0

while jogador!=computador:
    if jogador < computador:      
        print("Mais... Tenta outra vez:")
        jogador=int(input("Tente adivinhar qual número eu escolhi: "))
        tentativas+=1
    elif jogador > computador:       
        print("Menos... Tenta outra vez:")
        jogador=int(input("Tente adivinhar qual número eu escolhi: "))
        tentativas+=1

if tentativas==0:
    print("Uau, você acertou de primeira, parabéns!!!")
else:
    print(f"Parabéns, você acertou com {tentativas+1} tentativas!!!")