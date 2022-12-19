#Faça um programa que leia um número qualquer e mostre o seu fatorial

number = int(input("Type a number to know your factorial: "))
num=number

factorial = 1
while num>0:
    factorial = factorial * num
    num=num-1
    
print(f"The factorial of {number} is {factorial}")