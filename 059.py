#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso


def novos_numeros(x,y):
    x=int(input("X: "))
    y=int(input("Y: "))
    comando=int(input("Digite a opção desejada: "))
    print("\n")
    
def somar(x,y):
    return x + y

def multiplicar(x,y):
    return x * y

def maior(x,y):
    if x>y:
        return x
    if y>x:
        return y
    if x==y:
        return "Valores Iguais"

saida=1
x=int(input("X: "))
y=int(input("Y: "))
print("\n")
while saida!=5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
          ''')   
    comando=int(input("Digite a opção desejada: "))
    print("\n")
    if comando == 1:
        print(f"{x} + {y} = {somar(x,y)}\n")
    elif comando == 2:
        print(f"{x} * {y} = {multiplicar(x,y)}\n")
    elif comando == 3:
        maior = maior(x,y)
        if maior == x or maior == y:
            print(f"O maior número entre {x} e {y} é {maior}\n")
        elif maior == "Valores Iguais":
            print("Dois números iguais foram digitados!\n")
    elif comando == 4:
        novos_numeros(x,y)
    elif comando == 5:
        print("Programa finalizado!")
        break
    else:
        print("Comando Inválido, favor insira um novo comando: ")