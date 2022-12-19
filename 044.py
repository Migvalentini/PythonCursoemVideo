#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e 
# condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print("\033[35mBem Vindo a Loja Do Miguel\033[m")

preco = float(input("Digite o valor das compras: R$"))

print("\033[33mFormas de Pagamento: ")
print("[ 1 ] - À vista no dinheiro/cheque")
print("[ 2 ] - À vista no cartão")
print("[ 3 ] - Em até 2x no cartão")
print("[ 4 ] - 3x ou mais no cartão\033[m")

pagamento = int(input("Digite a forma de pagamento: "))

if pagamento == 1:
    print(f"O valor que antes era de R${preco} vai passar a ser de R${preco - (preco / 100 * 10)}")
elif pagamento == 2:
    print(f"O valor que antes era de R${preco} vai passar a ser de R${preco - (preco / 100 * 5)}")
elif pagamento == 3:
    print(f"O valor de cada parcela vai ser de R${preco/2}")
elif pagamento == 4:
    parcelas = int(input("Em quantas parcelas? "))
    valor = preco + (preco / 100 * 20)
    print(f"Sua compra será parcelada em {parcelas} parcelas de R${valor / parcelas}")
    print(f"Sua compra de R${preco} será de R${valor} no final")