import os
os.system('cls'if os.name == 'nt' else 'clear')

from clases.Login import verificar_acceso 
from clases.Menu import menu

booleana = verificar_acceso()

if booleana == True:
    n = menu()
    print(n)



    