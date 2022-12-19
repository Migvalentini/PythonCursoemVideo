#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a 
#quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

gamer = {}
matches = []
pos = 1
total = 0

gamer['name'] = str(input("Enter the gamer name: "))
amount_matches = int(input("Enter the amount of matches: "))
for match in range(1, amount_matches+1):
    goals_match = int(input(f"How much goals in the match {pos}? "))
    matches.append(goals_match)
    total += goals_match
    pos += 1
    
gamer['matches'] = matches 
gamer['total'] = total

print("-="*20)
print(gamer)
print("-="*20)
for k, v in gamer.items():
    print(f"The camp {k} has value {v}")
print("-="*20)
print(f"The gamer {gamer['name']} played {len(gamer['matches'])} matches")
for a, b in enumerate(gamer["matches"]):
    print(f"In the match {a}, the gamer {gamer['name']} scored {b} goals")
print(f"Was a total of {total} goals")          