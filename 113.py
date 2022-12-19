#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

'''
try: 
    operação
except TypeError:
    falhou
except ValueError:
    falhou
except OSError:
    falhou
else:
    deu certo
finally:
    deu certo/errado        
'''

from Módulos import coin113

whole = coin113.input_int("Enter a whole number: ")
real = coin113.input_float("Enter a real number: ")

print(f"You entered the whole number {whole} and the real number {real}")