#Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))

media = (n1 + n2) / 2

if media < 5:
    print(f"Com a média {media}, o aluno foi REPROVADO")
if 5 <= media <= 6.9:
    print(f"Com a média {media}, o aluno ficou de RECUPERAÇÃO")
if media >= 7:
    print(f"Com a média {media}, o aluno foi APROVADO")