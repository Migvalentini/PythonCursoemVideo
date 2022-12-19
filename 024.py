cidade = str(input("Digite a cidade: ")).strip()

teste = cidade[:5].upper() == "SANTO"

if teste == True:
    print("Começa com 'Santo'")
else: 
    print("N° começa com 'Santo'")
