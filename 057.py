#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo=str(input("Digite seu sexo [M/F]: ").strip().upper()[0])
while sexo not in "MF":
    print("Sexo Inválido, por favor digite 'M' para Masculino ou 'F' para Feminino")
    sexo=str(input("Digite seu sexo [M/F]: ").upper())

print(f"\033[0;32mSexo {sexo} validado com sucesso!\033[m")