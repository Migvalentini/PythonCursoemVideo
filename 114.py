#Crie um código em Python que teste se o site pudim está acessível pelo computador usado

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print("The website Pudim is currently unavailable")
else:
    print("Pudim is very hot")