#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def token(name="<unknown>", goals=0):
    if name == None:
        name = "<unknown>"
    print(f"The gamer {name} scored {goals} goals")

name = str(input("Enter the game name: "))
goals = str(input("Enter the number of goals: "))

if goals.isnumeric():
    goals = int(goals)
else: 
    goals = 0

if name.strip() == "":
    token(goals=goals)
else:
    token(name, goals)