#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) 
#e mostre a área do terreno

def calculate_area(width, length):
    area = width*length
    print(f"The area is {area} m²")

width = float(input("Enter the width: "))
length = float(input("Enter the length: "))
calculate_area(width, length)