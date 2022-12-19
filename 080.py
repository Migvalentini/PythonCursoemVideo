#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

list = []


for c in range(5):
    number = float(input("Enter a number: "))
    if c == 0 or number > list[-1]:
        list.append(number)
    else:
        pos = 0
        while pos < len(list):
            if number <= list[pos]:
                list.insert(pos, number)
                break
            pos += 1

print(list)