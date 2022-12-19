#Vamos criar um menu em Python, usando modularização.
#Vamos ver como fazer acesso a arquivos usando o Python.

from Módulos.Funções115 import *
from Módulos.coin113 import input_str, input_float
from time import sleep

file = "people.txt"

if not ExistFile(file):
    createFile(file)

while True:
    option = menu(["See registered people","Register new person","Clear people","Exit system"])
    if option == 1:
        print("Seeing registered people...")
        readFile(file)
        a = open(file, "rt")
        if a.read() == "":
            print("Empty File")
    elif option == 2:
        print("Registering new person...")
        while True:
            name = input_str("Enter a Name: ")
            age = input_float("Enter a Age: ")
            register(file, name, age)
            answer = str(input("Enter if you want register another person [Y/N]: ").upper().strip()[0])
            if answer == "N":
                break
    elif option == 3:
        print("Cleaning file...")
        clearFile(file)
    elif option == 4:
        print("Exiting system...")
        sleep(1)
        break
    else:
        print("\033[0;31mInvalid Answer, Enter a Valid Option\033[m")