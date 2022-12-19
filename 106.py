#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores

colors = (
    "\033[0;30m",
    "\033[0;31m",
    "\033[0;32m",
    "\033[0;33m",
    "\033[0;34m",
    "\033[0;35m",
    "\033[0;36m",
    "\033[0;37m",
    "\033[m",
)

def print_help(con):
    help(con)

def title(msg, color=0):
    print(colors[color], end="")
    size = len(msg)
    print("~" * size)
    print(msg)
    print("~" * size)
    print(colors[8], end="")
    
while True:
    title("Welcome to PyHelp", 4)
    print_help(input("Enter what object you want see: "))
    controller = str(input("Enter if you want continue [End to stop]: ")).upper()
    if controller == "END":
        break                                                                                                                                       
    
title("See you soon!", 4)