#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e 
# os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

controller = " "
list = []
even_list = []
odd_list = []

while controller != "N":
    number = int(input("Enter a number: "))
    list.append(number)
    controller = " "
    while controller not in "YyNn":
        controller = str(input("Do you want continue? ").upper().strip()[0])
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
    
print(f"The complete list is {list}")
print(f"The list of even numbers is {even_list}")
print(f"The list of odd numbers is {odd_list}")