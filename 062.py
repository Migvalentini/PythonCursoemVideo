#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos

first_term = int(input("Type the first term: "))
ratio = int(input("Type the ratio: "))

term = first_term
cont = 1
end = 1

while cont <= 10:
    print(term)
    cont+=1
    term+=ratio

while end != 0:        
    end = int(input("Hom much terms do you want write? "))
    cont = 1
    while cont <= end:
        term+=ratio
        print(term)
        cont+=1