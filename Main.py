import os
import sys
sys.path.append('AvanzadaII\Proyecto1\Clases')
os.system('cls'if os.name == 'nt' else 'clear')

from Clases.Login import verificar_acceso 
from Clases.Menu import menu
from Clases.Opciones import opcionesMenu

booleana = verificar_acceso()

if booleana == True:
    n = menu()
    opciones = opcionesMenu()
    opciones.opcion(n)
    