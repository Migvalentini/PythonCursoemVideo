#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notes(*note, situation):
    dict = {}
    list = []
    #biggest = smallest = cont = sum = 0
    for n in note:
        list.append(n)
        '''if cont == 0:
            biggest = smallest = n
        if n > biggest:
            biggest = n
        elif n < smallest:
            smallest = n
        sum += n
        cont += 1'''
    
    dict['notes'] = list
    dict['biggest'] = max(note)
    dict['smallest'] = min(note)
    dict['average'] = round(sum(note) / len(note), 2)
    dict['amount'] = len(note)
    
    if situation:
        if dict['average'] >= 7:
            dict['situation'] = "Good"
        elif dict['average'] >= 5:
            dict['situation'] = "Reasonable"
        else:
            dict['situation'] = "Bad"
        
    return dict
    
note = notes(10, 4, 3, 6, 9, situation=True)
print(note)