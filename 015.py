dias = float(input("Digite por quantos dias o carro foi alugado: "))
km = float(input("Digite por quantos quilômetros o carro foi alugado: "))

preco = 60 * dias + 0.15 * km

print("Um carro que foi alugado por {} dias e por {} km pagará {} reais".format(dias, km, preco))