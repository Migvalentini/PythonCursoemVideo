#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

tuple = ('Lénis', 1.75,
             'Borracha', 2,
             'Caderno', 15.90,
             'Esteie', 25,
             'Transferidor', 4.20,
             'Compasse', 9.99,
             'Mochila',  120.32,
             'Canetas', 22.30,
             'Livro', 34.90)
print("="*40)
print(f'{"PRICES LIST":^40}')
print("="*40)
for pos in range(0, len(tuple)):
    if pos % 2 == 0:
        print(f"{tuple[pos]:.<30}",f"R${tuple[pos+1]:>7.2f}")
print("="*40)