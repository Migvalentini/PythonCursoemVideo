#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

list = []
entered_numbers = 0
controller = " "

while controller != "N":
    number = float(input("Enter a number: "))
    list.append(number)
    entered_numbers += 1
    controller = " "
    while controller not in "YyNn":
        controller = str(input("Do you want continue? [Y/N]: ").upper().strip()[0])
    
print(list)
print(f"Was entered {entered_numbers} numbers")
list.sort(reverse=True)
print(f"The descending order is {list}")
if 5 in list:
    print("The number 5 is in the list!")
else:
    print("The number 5 isn't in the list!")
