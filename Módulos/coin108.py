def increase(num, percentage):
    return num + (num * percentage) / 100
    
def decrease(num, percentage):
    return num - (num * percentage) / 100
    
def double(num):
    return num * 2
    
def triple(num):
    return num * 3

def coin(num = 0, coin = "R$"):
    return f"{coin}{num:.2f}".replace('.',',')