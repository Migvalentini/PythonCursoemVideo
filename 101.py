#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def vote(year_birth):
    from datetime import datetime
    now = datetime.now().year - year_birth
    if 18 <= now  < 70:
        return f"With {now} years, the vote is MANDATORY"
    elif now >= 70 or 16 <= now < 18:
        return f"With {now} years, the vote is OPTIONAL"
    elif now < 16:
        return f"With {now} years, DON'T VOTE"
    
year_birth = int(input("Enter your of birth : "))
print(vote(year_birth))