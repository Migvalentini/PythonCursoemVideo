#Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 
# 2 para octal,
# 3 para hexadecimal.

n = int(input("Digite um número inteiro: "))

print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

conv = int(input("Base de Conversão: "))

if conv == 1:
    numero = bin(n)[2:]
elif conv == 2:
    numero = oct(n)[2:]
elif conv == 3:
    numero = hex(n)[2:]
else:
    print("Opção Inválida, Tente Novamente")
    
if conv == 1 or conv == 2 or conv == 3:    
    print(f"O número convertido é {numero}")