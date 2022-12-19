#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. 
#Para os inferiores ou iguais, o aumento é de 15%.
 
salario = float(input("Digite o salário do usuário: "))

if salario > 1250:
    aumento = salario + (salario/100*10)
else:
    aumento = salario + (salario/100*15)
    
print(f"O salário de R${salario} passa a ser R${aumento}")