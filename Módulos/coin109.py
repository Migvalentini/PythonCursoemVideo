def increase(num, percentage, formatting, coin = "R$"):
    if formatting == "True":
        return f"{coin}{(num + (num * percentage) / 100):.2f}".replace('.',',')
    elif formatting == "False":
        return num + (num * percentage) / 100
          
def decrease(num, percentage, formatting, coin = "R$"):
    if formatting == "True":
        return f"{coin}{(num - (num * percentage) / 100):.2f}".replace('.',',')
    elif formatting == "False":
        return num - (num * percentage) / 100
    
def double(num, formatting, coin = "R$"):
    if formatting == "True":
        return f"{coin}{(num * 2) :.2f}".replace('.',',')
    elif formatting == "False":
        return num * 2
    
def triple(num, formatting, coin = "R$"):
    if formatting == "True":
        return f"{coin}{(num * 3) :.2f}".replace('.',',')
    elif formatting == "False":
        return num * 3