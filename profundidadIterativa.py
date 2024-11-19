import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

def dfs_limitado(tablero, posicion, objetivo, limite, visitados, grafo, padre=None, nivel=0, expansiones=None, limite_expansiones=None):
    x, y = posicion
    filas, columnas = len(tablero), len(tablero[0])
    nodo_actual = f"({x},{y})"  

    if expansiones[0] >= limite_expansiones:
        return False

    if posicion == objetivo:
        print(f"Objetivo encontrado en {posicion}.")
        return True

    if limite <= 0:
        return False

    visitados.add(posicion)
    expansiones[0] += 1

    grafo.add_node(nodo_actual, nivel=nivel)
    if padre is not None:
        grafo.add_edge(padre, nodo_actual)

    mostrar_arbol_jerarquico(grafo)

    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        hijo = (nx, ny)

        if (0 <= nx < filas and 0 <= ny < columnas and
            tablero[nx][ny] != 1 and hijo not in visitados):
            if dfs_limitado(tablero, hijo, objetivo, limite - 1, visitados, grafo, nodo_actual, nivel + 1, expansiones, limite_expansiones):
                return True

    visitados.remove(posicion)
    return False

def mostrar_arbol_jerarquico(grafo):
    pos = graphviz_layout(grafo, prog="dot")
    plt.clf()
    plt.title("Profundidad iterativa", fontsize=16)
    nx.draw(
        grafo,
        pos,
        with_labels=True,
        node_size=1500,
        node_color="lightblue",
        font_size=10,
        font_weight="bold",
        arrows=False
    )
    
    plt.draw()
    plt.pause(0.5)

def busqueda_profundidad_iterativa(tablero, limite_expansiones):
    filas, columnas = len(tablero), len(tablero[0])
    inicio, objetivo = None, None

    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] == 2:
                inicio = (i, j)
            elif tablero[i][j] == 3:
                objetivo = (i, j)

    if not inicio or not objetivo:
        raise ValueError("No se encontró el ratón (2) o el queso (3) en el tablero.")

    limite = 0
    grafo = nx.DiGraph()
    expansiones = [0]

    plt.ion()

    while expansiones[0] < limite_expansiones:
        print(f"Buscando con límite de profundidad: {limite}")
        visitados = set()
        if dfs_limitado(tablero, inicio, objetivo, limite, visitados, grafo, None, 0, expansiones, limite_expansiones):
            plt.ioff()
            plt.show()
            return True
        limite += 1

    plt.ioff()
    plt.show()
    return False

def ejecutar_busqueda(tablero, limite_expansiones):
    
    return busqueda_profundidad_iterativa(tablero, limite_expansiones)

# Ejemplo de uso
if __name__ == "__main__":
    tablero = [
        [0, 0, 0, 0],
        [0, 1, 1, 3],
        [2, 1, 0, 0],
        [0, 0, 0, 1]
    ]

    #resultado = ejecutar_busqueda(tablero, limite_expansiones)

