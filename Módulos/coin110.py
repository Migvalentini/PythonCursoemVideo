def increase(num, percentage, formatting= True):
    response = num + (num * percentage) / 100
    if formatting:
        return formatted(response)
    else:
        return response
          
def decrease(num, percentage, formatting= True):
    response = num - (num * percentage) / 100
    if formatting:
        return formatted(response)
    else:
        return response
    
def double(num, formatting= True):
    response = num * 2
    if formatting:
        return formatted(response)
    else:
        return response
    
def triple(num, formatting= True):
    response = num * 3
    if formatting:
        return formatted(response)
    else:
        return response
    
def formatted(num, coin= "R$"):
    return f"{coin}{num:.2f}".replace('.',',')

def resume(num, percentage):
    print("-" * 40)
    print("VALUE RESUME:".center(40))
    print(f"Price Analyzed: \t\t{formatted(num)}")
    print(f"Double the Price: \t\t{double(num)}")
    print(f"Triple the Price: \t\t{triple(num)}")
    print(f"Increasing {percentage:.0f}%, the number is: \t{increase(num, percentage)}")
    print(f"Decreasing {percentage:.0f}%, the number is: \t{decrease(num, percentage)}")
    print("-" * 40)