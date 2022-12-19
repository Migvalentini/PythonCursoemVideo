#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

def print_message(message):
    print(f"="*len(message))
    print(f"{message}")
    print(f"="*len(message))
    
    
message = str(input("Enter a message: "))
print_message(message)