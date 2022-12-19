#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

from random import randint

def sort(a):
    for n in range(5):
        numbers.append(randint(1, 10))
    print(f"The original list is {numbers}")

def add_pair(a):
    sum = 0
    print("The even numbers are: ")
    for num in numbers:     
        if num % 2 == 0:
            sum += num
            print(num, end = " ")
    print(f"\nThe sum of the even numbers is {sum}")

numbers = []
sort(numbers)
add_pair(numbers)