def input_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mWrong number, enter a valid number!\033[m")
            continue
        else:
            return n
            
def input_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mWrong number, enter a valid number!\033[m")
            continue
        else:
            return n
        
def input_str(msg):
    while True:
        try:
            n = str(input(msg))
            if len(n.replace(" ","")) == 0 or n.isdigit():
                print("\033[0;31mWrong name, enter a valid name!\033[m")
                continue
        except:
            print("\033[0;31mWrong name, enter a valid name!\033[m")
            continue
        else:
            return n
        
input_str("Name: ")