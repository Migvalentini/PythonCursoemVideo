#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

value = int(input("Enter how much you want withdraw: "))
total = value
banknote = 50
totbnknt = 0
while True:
    if total >= banknote:
        total -= banknote
        totbnknt += 1
    else:
        if totbnknt > 0:
            print(f'Total of {totbnknt} banknotes of R${banknote}')
        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1
        totbnknt = 0
        if total == 0:
            break