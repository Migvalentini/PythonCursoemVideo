#Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

team = []
gamer = {}
matches = []

controller = " "

while controller != "N":
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
    team.append(gamer.copy())
    gamer.clear()
    controller = " "
    while controller not in "YyNn":
        controller = str(input("Do you want continue? ")).upper().strip()[0]

print("Cod     Name:         Goals:     Total:")        
for num, game in enumerate(team):
    print(f"{num:>}        {game['name']}        {game['matches']}      {game['total']}")
    
while True:
    selected_gamer = int(input("Enter what player do you want see the information: "))
    if selected_gamer == 999:
        break
    print(f"Information about {team[selected_gamer]['name']}")
    for match in team[selected_gamer]['matches']:
        print(f"In the {match}° game, the gamer {team[selected_gamer]['name']} scored {team[selected_gamer]['matches'][match-1]} goals")