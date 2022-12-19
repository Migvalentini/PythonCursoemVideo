#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

total = 0
over_1000 = 0
cheapest_product = 0
cheapest_product_name = " "

while True:
    name_product = str(input("Enter the product name: "))
    price_product = float(input("Enter the product price: "))
    if total == 0:
        cheapest_product = price_product
    if price_product < cheapest_product:
        cheapest_product = price_product
        cheapest_product_name = name_product
    if price_product > 1000:
        over_1000 += 1
    total += price_product   
    controler = " " 
    while controler not in "CS":
        controler = str(input("Enter if you want continue or to stop : ")).strip().upper()[0]
    if controler == "S":
        break
    
print(f"The total is R${total}")
print(f"{over_1000} products cost less than R$1000")
print(f"The cheapest product is {cheapest_product_name}")