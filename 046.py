#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 
#10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)    
print("\033[0;30mS\033[0;31mO\033[0;32mL\033[0;33mT\033[0;34mA \033[0;35mO \033[0;36mR\033[0;37mOJ\033[0;31mÃ\033[0;30mO!")