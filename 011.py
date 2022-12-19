largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area / 2

print("A dimensão da parede é",largura,"x",altura)
print("A área da parede é",area)
print("Você precisa de",tinta,"litros para pintar a parede")