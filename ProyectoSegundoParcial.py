# Proyecto Segundo Parcial
# Desarrolladores:
#   Fabián Camp Mussa - A01378565 // https://github.com/fcampm
#   Adrián Méndez López -  A01379228  // https://github.com/AdrianML
# Fecha: Abril 9, 2018.

# Bibliotecas utilizadas
import csv
import math

def menuPrincipal():
    print(" =============================== ")
    print("| Menu Proyecto Segundo Parcial |")
    print(" =============================== ")
    print("| 1. Busqueda de numeros en     |")
    print("|     un conjunto de datos      |")
    print("| 2. Algoritmo BFS y DFS        |")
    print("| 3. Salir                      |")
    print(" =============================== ")

def menuGrafos():
    print(" ===================== ")
    print("| Algoritmo BFS y DFS |")
    print(" ===================== ")
    print("| 1. Algoritmo BFS    |")
    print("| 2. Algoritmo DFS    |")
    print("| 3. Menu Principal   |")
    print(" ===================== ")

def grafos():
    menuGrafos()
    opcionGrafos = int(input("Seleccione una opcion: "))
    if opcionGrafos == 1:
        algortimoBFS()
    elif opcionGrafos == 2:
        algoritmoDFS()
    elif opcionGrafos == 3:
        return

def algortimoBFS():


def menuNumeros():
    #Lectura del txt
    leeArchivo()
    #Determinar si esta ordenado o no
    revisaLista()
    #Pedir numero al usuario
    #Escoger algoritmo, (ordenado-binary / desordenado-a escoger)
    #Mostrar dato buscado, numero de operaciones elementales, numero de casilla donde se ubico

def leeArchivo():
    lista = open("Datos.txt","r") as ListaNum
    reader = csv.reader(ListaNum)
    for line in reader:
       ListaNum.append(line)

#def revisaLista(lista):
#

def main():
    while(True):
        menuPrincipal()
        opcionMenuPrincipal = int(input("Seleccione una opcion: "))
        if opcionMenuPrincipal == 1:
            menuNumeros()
        elif opcionMenuPrincipal == 2:
            grafos()
        elif opcionMenuPrincipal == 3:
            print("Gracias por su preferencia vuelva pronto :)")
            break
        else:
            print("No es una opcion valida")
main()
