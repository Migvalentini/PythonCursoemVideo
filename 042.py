#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

a = float(input("Digite o 1° lado do triângulo: "))
b = float(input("Digite o 2° lado do triângulo: "))
c = float(input("Digite o 3° lado do triângulo: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Triângulo Equilátero")
    elif a != b and a != c and b != c:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isósceles")
else:
    print("Não é possível formar um triângulo com essas medidas")