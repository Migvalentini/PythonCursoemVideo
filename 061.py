#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

first_term = int(input("Type the first term: "))
ratio = int(input("Type the ratio: "))

term = first_term
cont=1
while cont <= 10:
    print(term)
    cont+=1
    term+=ratio