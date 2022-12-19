#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a 
#validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def intup_int(n:str):
    while True:
        n = str(input())
        if n.isnumeric():
            return n
        else:
            print("Error!")
        
        

n = intup_int("Enter a number: ")
print(f"You entered the number {n}")