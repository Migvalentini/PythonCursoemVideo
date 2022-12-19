from random import shuffle

a1 = str(input("Digite o primeiro aluno: "))
a2 = str(input("Digite o segundo aluno: "))
a3 = str(input("Digite o terceiro aluno: "))
a4 = str(input("Digite o quarto aluno: "))

lista = [a1,a2,a3,a4]
shuffle(lista)

print("A sequência sorteada foi: {}".format(lista))