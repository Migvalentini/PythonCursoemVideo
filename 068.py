#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
wins = 0
user_play = " "
user_num = 3
while True:
    computer = randint(1,2)
    while user_num != 1 and user_num != 2:
        user_num = int(input("Enter your play [1/2]: "))
    while user_play not in "PpIi":
        user_play = str(input("Enter you you want par or ímpar [P/I]: ").upper().split()[0])
    sum = computer + user_num
    print(f"Your choiced = {user_num}\nYour play = {user_play}\nComputer choiced {computer}\nSum = {sum}")
    if sum % 2 == 0 and user_play == "P" or sum % 2 == 1 and user_play == "I":
        print("You WON!")
        wins += 1
    elif sum % 2 == 0 and user_play == "I" or sum % 2 == 1 and user_play == "P":
        print("You LOST!")
        break
    
print(f"You won {wins} times!")