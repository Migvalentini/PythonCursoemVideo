#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108

from Módulos import coin109

num = float(input("Enter a number: "))
percentage = float(input("Enter a percentage: "))
formatting = str(input("Enter if you want the formatting [True/False]: "))
print(f"Increasing {percentage:.0f}%, the number is: {coin109.increase(num, percentage, formatting=formatting)}")
print(f"Decreasing {percentage:.0f}%, the number is: {coin109.decrease(num, percentage, formatting=formatting)}")
print(f"The double of {num:.0f} is: {coin109.double(num, formatting=formatting)}")
print(f"The triple of {num:.0f} is: {coin109.triple(num, formatting=formatting)}")