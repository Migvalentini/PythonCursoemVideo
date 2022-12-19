#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero=int(input("Digite um número para saber sua tabuada: "))
for c in range(1,11):
    print(numero,"x",c,"=",numero*c)