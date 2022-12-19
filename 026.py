frase = str(input("Digite uma Frase: ")).strip().lower()

print("A letra 'A' aparece",frase.count("a"),"vezes")
print("A primeira letra 'A' aparece na posição",frase.find("a")+1)
print("A última letra 'A' aparece na posição",frase.rfind("a")+1)