import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

def buscar_en_laberinto(laberinto, N):
    gano=False
    
    def calculo_profundidad_limite():
        return len(laberinto) * len(laberinto[0])

    def busqueda_limitada_profunidad(inicio, profundidad_maxima):
        filas, columnas = len(laberinto), len(laberinto[0])
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        nodos_visitados = set()
        grafo = nx.DiGraph()

        def es_valido(x, y):
            return 0 <= x < filas and 0 <= y < columnas and laberinto[x][y] != 1 and (x, y) not in nodos_visitados

        def buscar(posicion, profundidad, pasos_realizados, padre=None):
            
            if profundidad > profundidad_maxima or pasos_realizados >= N:
                return

            x, y = posicion
            nodo_actual = f"({x},{y})"
            nodos_visitados.add(posicion)
            grafo.add_node(nodo_actual, nivel=profundidad)
            if padre:
                grafo.add_edge(padre, nodo_actual)

            mostrar_arbol_jerarquico(grafo)

            for dx, dy in movimientos:
                nuevo_x, nuevo_y = x + dx, y + dy
                if es_valido(nuevo_x, nuevo_y):
                    buscar((nuevo_x, nuevo_y), profundidad + 1, pasos_realizados + 1, nodo_actual)

        buscar(inicio, 0, 0)
        return nodos_visitados

    def mostrar_arbol_jerarquico(grafo):
        pos = graphviz_layout(grafo, prog="dot")
        plt.clf()
        plt.title("Árbol de búsqueda limitada por profundidad", fontsize=16)
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

    inicio = next((i, j) for i, fila in enumerate(laberinto) for j, valor in enumerate(fila) if valor == 2)
    plt.ion()
    grafo = busqueda_limitada_profunidad(inicio, calculo_profundidad_limite())
    plt.ioff()
    plt.show()


    nodo_a_buscar = (1,3)

    if nodo_a_buscar in grafo:
        gano=True



    return gano


laberinto = [
    [0, 0, 0, 0],
    [0, 1, 1, 3],
    [2, 1, 0, 0],
    [0, 0, 0, 1]
]
#achu=buscar_en_laberinto(laberinto, 8)
