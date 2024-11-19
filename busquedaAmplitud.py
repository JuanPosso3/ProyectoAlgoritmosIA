import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
from collections import deque

def buscar_camino_bfs(matriz, max_profundidad):
    def transformar():
        grafo = {}
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 1:  # No considerar paredes
                    continue
                vecinos = []
                if i > 0 and matriz[i-1][j] != 1:  
                    vecinos.append((i-1, j))
                if i < len(matriz) - 1 and matriz[i+1][j] != 1: 
                    vecinos.append((i+1, j))
                if j > 0 and matriz[i][j-1] != 1:  
                    vecinos.append((i, j-1))
                if j < len(matriz[i]) - 1 and matriz[i][j+1] != 1:  
                    vecinos.append((i, j+1))
                grafo[(i, j)] = vecinos
        return grafo

    def encontrar_posicion(valor):
        for i, fila in enumerate(matriz):
            for j, celda in enumerate(fila):
                if celda == valor:
                    return (i, j)
        return None

    def busqueda_amplitud_limitada(grafo, inicio, final):
        visitados = set()
        cola = deque([(inicio, 0)])
        padres = {inicio: None}
        arbol = {}
        grafo_visual = nx.DiGraph()

        def mostrar_arbol():
            pos = graphviz_layout(grafo_visual, prog="dot")
            plt.clf()
            plt.title("Algoritmo de Búsqueda en Amplitud", fontsize=16)
            nx.draw(
                grafo_visual,
                pos,
                with_labels=True,
                node_size=1500,
                node_color="skyblue",
                font_size=10,
                font_weight="bold",
                arrows=True,
            )
            plt.draw()
            plt.pause(0.5)

        grafo_visual.add_node(f"{inicio}")
        mostrar_arbol()

        while cola:
            vertice, profundidad = cola.popleft()

            if profundidad >= max_profundidad:
                continue

            if vertice == final:
                camino = []
                while vertice is not None:
                    camino.append(vertice)
                    vertice = padres[vertice]
                return camino[::-1], arbol

            if vertice in visitados:
                continue

            visitados.add(vertice)
            arbol[vertice] = padres.get(vertice, None)

            for vecino in grafo[vertice]:
                if vecino not in visitados:
                    cola.append((vecino, profundidad + 1))
                    padres[vecino] = vertice
                    grafo_visual.add_node(f"{vecino}")
                    grafo_visual.add_edge(f"{vertice}", f"{vecino}")
                    mostrar_arbol()

        return None, arbol

    inicio = encontrar_posicion(2)
    final = encontrar_posicion(3)
    grafo = transformar()

    plt.ion()
    camino, arbol = busqueda_amplitud_limitada(grafo, inicio, final)
    plt.ioff()
    plt.show()

    if camino:
        print("\nCamino encontrado:", camino)
        camino=True
    else:
        print("No se encontró un camino dentro del límite de profundidad.")

    """
    print("\nÁrbol de búsqueda:")
    for nodo, padre in arbol.items():
        print(f"{nodo}: {padre}")
    """

    return camino

"""
matriz = [
    [0, 0, 0, 0],
    [0, 1, 1, 3],
    [2, 1, 0, 0],
    [0, 0, 0, 1],
]
"""



