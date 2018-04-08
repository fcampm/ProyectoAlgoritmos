def leeArchivo():
    listaNodos = []
    for n in open('Graphs.txt').read().split():
        a, b = n.strip('()').split(',')
        listaNodos.append((int(a), int(b)))
    print(listaNodos)
    return listaNodos


