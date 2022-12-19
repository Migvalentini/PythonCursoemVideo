from Módulos import coin113

def ExistFile(name):
    try:
        a = open(name, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def createFile(name):
    try:
        a = open(name, "wt+")
        a.close()
    except:
        print("\033[0;31mAn Error Occurred!\033[m")
    else:
        print(f"File {name} Created Successfully")

def line():
    print("-"*30)

def header(txt="MEIN MENU"):
    print("\033[0;36m")
    line()
    print(txt.center(30))
    line()
    print("\033[m")

def menu(list):
    header()
    for i, c in enumerate(list):
        print(f"\033[0;33m{i+1}: \033[0;30m{c}\033[m")
    print()
    option = coin113.input_int("Enter you option: ")
    return option

def readFile(name):
    try:
        a = open(name, "rt")
    except:
        print("An Error Occurred")
    else:
        header("People Registered")
        for person in a:
            info = person.split(";")
            info[1] = info[1].replace("\n", "")
            print(f"{info[0]:<20} {info[1]:>3} years")
    finally:
        a.close()
            
def register(file, name, age):
    try:
        a = open(file, "at")
    except:
        print("An Error Occurred When Opening File")
    else:
        try:
            a.write(f"{name};{age}\n")
        except:
            print("An Error Occurred When Writing to the File")
            
def clearFile(file):
    try:
        a = open(file, "wt")
    except:
        print("An Error Occurred When Opening File")
    else:
        a.write("")