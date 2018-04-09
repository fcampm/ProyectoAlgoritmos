# Proyecto Segundo Parcial
# Desarrolladores:
#   Fabián Camp Mussa - A01378565 // https://github.com/fcampm
#   Adrián Méndez López -  A01379228  // https://github.com/AdrianML
# Fecha: Abril 9, 2018.

# Bibliotecas utilizadas
import csv
import math

nodos = []

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
    print("| 1. Algoritmo DFS    |")
    print("| 2. Algoritmo BFS    |")
    print("| 3. Menu Principal   |")
    print(" ===================== ")

def grafos():
    menuGrafos()
    opcionGrafos = int(input("Seleccione una opcion: "))
    if opcionGrafos == 1:
        algortimoDFS()
    elif opcionGrafos == 2:
        algoritmoBFS()
    elif opcionGrafos == 3:
        return

# Método para crear un grafo y meter información a los grafos
# Bibliografía del código: https://sites.google.com/site/programacioniiuno/temario/unidad-5---grafos/algoritmos-de-bsquedas
from collections import deque

class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)

def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2):
    relacionarUnilateral(grafo, elemento1, elemento2)
    relacionarUnilateral(grafo, elemento2, elemento1)

def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)

def profundidadPrimero(grafo, elementoInicial, funcion, elementosRecorridos = []):
    if elementoInicial in elementosRecorridos:
        return
    funcion(elementoInicial)
    elementosRecorridos.append(elementoInicial)
    for vecino in grafo.relaciones[elementoInicial]:
        profundidadPrimero(grafo, vecino, funcion, elementosRecorridos)

def anchoPrimero(grafo, elementoInicial, funcion, cola = deque(), elementosRecorridos = []):
    if not elementoInicial in elementosRecorridos:
        funcion(elementoInicial)
        elementosRecorridos.append(elementoInicial)
        if(len(grafo.relaciones[elementoInicial]) > 0):
            cola.extend(grafo.relaciones[elementoInicial])
    if len(cola) != 0 :
        anchoPrimero(grafo, cola.popleft(), funcion, cola, elementosRecorridos)



def cargarGrafo():
    numeroNodos = int(input("Digite el numero total de nodos: "))

    for i in range(numeroNodos):
        valorNodo = int(input("Introduzca el valor del nodo" + str(i+1) + " :" ))
        nodos.append(valorNodo)

def algortimoDFS():

    cargarGrafo()

    grafo = Grafo()
    for nodo in range(len(nodos)):
        agregar(grafo, nodos[nodo])

    relaciones = int(input("Introduzca el numero de relaciones del grafo: "))
    for i in range(relaciones):
        nodo1 = int(input("Digite nodo 1: "))
        nodo2 = int(input("Digite nodo 2: "))
        relacionar(grafo, nodo1, nodo2)

    nodoInicio = int(input("Seleccione el nodo de inicio: "))
    profundidadPrimero(grafo, nodoInicio, imprimir)


def imprimir(elemento):
    print (elemento)

def algoritmoBFS():

    cargarGrafo()

    grafo = Grafo()
    for nodo in range(len(nodos)):
        agregar(grafo, nodos[nodo])

    relaciones = int(input("Introduzca el numero de relaciones del grafo: "))
    for i in range(relaciones):
        nodo1 = int(input("Digite nodo 1: "))
        nodo2 = int(input("Digite nodo 2: "))
        relacionar(grafo, nodo1, nodo2)

    nodoInicio = int(input("Seleccione el nodo de inicio: "))
    anchoPrimero(grafo, nodoInicio, imprimir)

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
    return

def buscaNumero():
    num = int(input("Numero a buscar: "))
    return num


def sequentialSearch(lista, num):
    i = 0
    print("<SEQUENTIAL SEARCH>")
    for i in range(len(lista)):
        if lista[i] == num:
            print("El numero " + str(num) + " se encontro en la posicion " + str(i+1) +" y se realizaron " + str(i+1) + " pasos elementales, (comparaciones).")
            return
    print("El numero " + str(num) + " no esta en la lista")

def binarySearch(lista, num):
    primer = 0
    ultimo = len(lista) - 1
    count = 0
    print("<BINARY SEARCH>")
    while primer <= ultimo:
        i = (primer + ultimo) // 2
        if lista[i] == num:
            print ("El numero " + str(num) + " se encontro en la posicion " + str(i+1) +" y se realizaron " + str(count) + " pasos elementales, (comparaciones).")
            return
        elif lista[i] > num:
            count +=1
            ultimo = i - 1
        elif lista[i] < num:
            count +=1
            primer = i + 1
    print("El numero " + str(num) + " no esta en la lista")
    return

def leeArchivo():
    listaNum = []
    with open("Datos.txt") as Lista:
        #reader = csv.reader(Lista)
        for line in Lista.read().split(","):
            listaNum.append(int(line))
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
