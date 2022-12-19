#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

list_principal = []
list_data = []
controller = " "
biggest = smallest = 0

while controller != "N":
    list_data.append(str(input("Enter a name: ")))
    list_data.append(float(input("Enter your weight: ")))
    if len(list_principal) == 0:
        smallest = biggest = list_data[1]
    else:
        if list_data[1] > biggest:
            biggest = list_data[1]
        elif list_data[1] < smallest:
            smallest = list_data[1]
    list_principal.append(list_data[:])
    list_data.clear()
    controller = " "
    while controller not in "YyNn":
        controller = str(input("Enter if you want continue: ").upper().strip()[0])

print(f"{len(list_principal)} people were registered")
print(f"The heaviest person has {biggest}kg")
print("The heaviest person are: ",end = "")
for people in list_principal:
    if people[1] == biggest:
        print(people[0], end = " ")
        
print(f"\nThe lightest person has {smallest}kg")
print("The lightest person are: ",end = "")
for people in list_principal:
    if people[1] == smallest:
        print(people[0], end = " ")