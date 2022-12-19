#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo. 

while True:
    num = int(input("Enter a number to know your multiplication table: "))
    if num < 0:
        break
    for c in range(10):
        print(num,"X",c+1,"=",(c+1)*num)
        
print("A negative number was entered, FINISHED PROGRAM!")