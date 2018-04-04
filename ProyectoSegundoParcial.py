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

#def algortimoBFS():


def menuNumeros():
    #Lectura del txt
    lista = leeArchivo()
    #Pedir numero al usuario y buscarlo / Algoritmo, (ordenado-binary / desordenado-a escoger)
    num = buscaNumero()
    #Revisa si la lista esta ordenada o no
    check = revisaLista(lista)
    #Seleccion de Algoritmo
    if check == True:
        #Binary Search
        binarySearch(lista, num)
    else:
        #Sequential Search
        sequentialSearch(lista, num)
    #Volver al menu principal
    print("\n")
    main()

def buscaNumero():
    num = int(input("Numero a buscar: "))
    return num
    

def sequentialSearch(lista, num):
    i = 0
    print("<SEQUENTIAL SEARCH>")
    while i < len(lista):
        if lista[i] == num:
            print("El numero " + num + " se encontro en la posicion " + i +" y se realizaron " + i + " pasos elementales, (comparaciones).")
        else:
            i +=1

def binarySearch(lista, num):
    primer = 0
    ultimo = len(lista) - 1
    count = 0
    print("<BINARY SEARCH>")
    while primer <= ultimo == True:
        i = (primer + ultimo) // 2
        if lista[i] == num == True:
            print ("El numero " + num + " se encontro en la posicion " + i +" y se realizaron " + count + " pasos elementales, (comparaciones).")
            return
        elif lista[i] > num == True:
            count +=1
            ultimo = i - 1
        elif lista[i] < num == True:
            count +=1
            primer = i + 1
        else:
            print("El numero a buscar no se encuentra en la lista")
            return

def leeArchivo():
    listaNum = []
    with open("Datos.txt") as Lista:
        reader = csv.reader(Lista)
        for line in reader:
            listaNum.append(line)
    print("Archivo Leido")
    return listaNum

def revisaLista(lista):
    x = sorted(lista)
    if x == lista:
        print("La lista esta ordenada")
        return True
    else:
        print("La lista no esta ordenada")
        return False

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
