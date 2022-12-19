#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente

list = [[],[]]

for n in range(7):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        list[0].append(number)
    else:
        list[1].append(number)
        
list[0].sort()
list[1].sort()
print(f"The ascending order of odd numbers is {list[0]}")
print(f"The ascending order of even numbers is {list[1]}")