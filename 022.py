from time import sleep

nome = input("Digite seu nome completo: ")

print("Analisando seu nome...")
sleep(1)
print("Seu nome em letras maiúsculas é:",nome.upper())
print("Seu nome em letras maiúsculas é:",nome.lower())
print("Seu nome tem",len(nome)-nome.count(" "),"letras")
print("Seu primeiro nome tem",nome.find(" "),"letras")