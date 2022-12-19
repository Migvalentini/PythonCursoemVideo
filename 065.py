#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi 
# o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

sum = 0
divider = 0
biggest = 0
smallest = 0
stop = "Y"
while stop == "Y":
    number = int(input("Enter a number: "))
    if sum == 0:
        smallest = number
    stop = str(input("Do you want continue [Y/N]? ").upper())
    while stop not in "YN":
        print("Wrong letter, type a possible letter!")
        stop = str(input("Do you want continue [Y/N]? ").upper())
    sum = sum + number
    divider += 1
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number
        
print(f"You typed {divider} numbers and the average is {sum/divider}. Biggest number is {biggest} and smallest is {smallest}")