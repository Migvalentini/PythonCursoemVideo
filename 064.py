# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a 
#condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

stop = 0
sum = 0
numbers = 0
while stop != 999:
    stop = int(input("Type a number [999 to stop]: "))
    sum = sum + stop
    numbers+=1
    
print(f"Were type {numbers - 1} numbers and your sum is {sum - 999}")