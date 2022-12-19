#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e 
#que se encontram no intervalo de 1 até 500.

soma,num=0,0
for c in range(1,501):
    if c%3==0 and c%2==1:
        soma=soma+c
        num+=1
        
print(f"A soma dos {num} números é {soma}")