#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('aprender', 'linguagem', 'python','curso', 'gratis', 'estudar', 'praticar','trabalhar', 'mercado', 'programador', 'futuro')

for word in words:
    print(word,":",end=" ")
    for letter in word:
        if letter == 'a':
            print('a',end=" ")
        if letter == 'e':
            print('e',end=" ")
        if letter == 'i':
            print('i',end=" ")
        if letter == 'o':
            print('o',end=" ")
        if letter == 'u':
            print('u',end=" ")
    print("\n")