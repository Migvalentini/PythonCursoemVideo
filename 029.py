velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado e deve pagar {multa} reais")
else:
    print("Tenha uma Boa Viagem!")