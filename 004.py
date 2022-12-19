algo = input("Digite algo: ")

print("Classe:",type(algo))
print("Só tem espaços?",algo.isspace())
print("É numérico?",algo.isnumeric())
print("É alfabético?",algo.isalpha())
print("É alfanumérico?",algo.isalnum())
print("É todo maiúsculo?",algo.isupper())
print("É todo minúsculo?",algo.islower())