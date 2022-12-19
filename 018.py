from math import sin, cos, tan, radians, trunc

numero = float(input("Digite um número: "))

seno = round(sin(radians(numero)),2)
cosseno = round(cos(radians(numero)),2)
tangente = round(tan(radians(numero)),2)

print("O seno de {} é {}".format(trunc(numero),seno))
print("O cosseno de {} é {}".format(trunc(numero),cosseno))
print("A tangente de {} é {}".format(trunc(numero),tangente))