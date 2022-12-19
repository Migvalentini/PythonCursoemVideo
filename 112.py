#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() 
#que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários

from Módulos import coin112 

num = coin112.inputCoin("Enter a price: ")
percentage = float(input("Enter a percentage: "))

print(coin112.resume(num, percentage))