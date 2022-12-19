#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = round(float(input("\033[0;34mDigite o valor da casa:\033[m ")))
salario = round(float(input("\033[0;34mDigite o salário do usuário:\033[m ")))
ano = round(float(input("\033[0;34mDigite em quantos anos o usuário irá pagar:\033[m ")))

prestacao = round(casa / (ano * 12),2)

print(f"Recebendo R${salario} por mês e pagando a casa de R${casa} em {ano} anos, a parcela será de R${prestacao}")

if prestacao < salario / 100 * 30:
    print("\033[0;32mEmpréstimo Concedido\033[m")
else:
    print("\033[0;31mEmpréstimo Negado\033[m")