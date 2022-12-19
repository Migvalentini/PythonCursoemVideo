#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
#mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

soma_idades=0
idade_homem_velho=0
homem_mais_velho=""
mulher=0
for c in range(1,5):
    print(f"---{c}° PESSOA---")
    nome=str(input("Digite o nome da pessoa: "))
    idade=float(input("Digite a idade da pessoa: "))
    sexo=str(input("Digite o sexo da pessoa (M/F): ").upper())
    soma_idades=soma_idades+idade
    if c==1 and sexo=="M":
        homem_mais_velho=nome
        idade_homem_velho=idade
    if sexo=="M" and idade>idade_homem_velho:
        homem_mais_velho=nome
        idade_homem_velho=idade
    if sexo=="F" and idade<20:
        mulher+=1
print(f"O homem mais velho é o {homem_mais_velho} e ele tem {idade_homem_velho} anos")
print(f"A média das idades é: {soma_idades/c}")
print(f"Há {mulher} mulheres mais novas que 20 anos")