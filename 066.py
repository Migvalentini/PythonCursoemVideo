#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)

numbers = 0
sum = 0
while True:
    number = float(input("Type a number: "))
    if number == 999: 
        break
    numbers += 1
    sum = sum + number

print(f"Were typed {numbers} numbers and the sum is {sum}")