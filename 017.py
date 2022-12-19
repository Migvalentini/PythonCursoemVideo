from math import sqrt

cateto_adj = float(input("Digite o valor do cateto adjacente: "))
cateto_opo = float(input("Digite o valor do cateto oposto: "))

hipotenusa = sqrt(cateto_adj**2 + cateto_opo**2)

print("A hipotenusa mede {}".format(hipotenusa))