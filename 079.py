#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

list = []
controller = " "

while controller != "N":
    number = float(input("Enter a number: "))
    if number not in list:
        list.append(number) 
    else:
        print("Number yet entered!") 
    controller = " "
    while controller not in "YyNn":
        controller = str(input("Enter if you want stop or continue [Y/N]: ").upper().strip()[0])

list.sort()        
print(f"The ascending order is: {list}")