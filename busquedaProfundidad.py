import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout


def busqueda_profundidad(matriz, arbol_recibido=None, limite_expansiones=8):
    gano=False
    def encontrar_inicio_meta():
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 3:
                    meta = (i, j)
                elif matriz[i][j] == 2:
                    inicio = (i, j)
        return inicio, meta

    def obtener_ultimo_nodo(arbol):
        nodos = list(arbol.keys())
        nodos.sort(key=lambda x: (x[1], x[0]))
        return nodos[-1]

    def mostrar_arbol():
        pos = graphviz_layout(grafo, prog="dot")
        plt.clf()
        plt.title("Algoritmo Búsqueda en Profundidad", fontsize=16)
        nx.draw(
            grafo,
            pos,
            with_labels=True,
            node_size=1500,
            node_color="lightgreen",
            font_size=10,
            font_weight="bold",
            arrows=True
        )
        plt.draw()
        plt.pause(0.5)

    def busqueda(posicion_actual):
        nonlocal expansiones, limite_excedido,gano

        if limite_excedido or posicion_actual in nodos:
            return False

        nodos.append(posicion_actual)
        expansiones += 1

        if expansiones > limite_expansiones:
            limite_excedido = True
            return False

        if posicion_actual == meta:
            gano=True
            return gano

        fila, columna = posicion_actual

        for mov_fil, mov_col in movimientos:
            nueva_fila = fila + mov_fil
            nueva_columna = columna + mov_col

            if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]):
                if matriz[nueva_fila][nueva_columna] != 1:
                    movimiento = (nueva_fila, nueva_columna)
                    if movimiento not in arbol and not limite_excedido:
                        arbol[movimiento] = posicion_actual
                        grafo.add_node(f"{movimiento}")
                        grafo.add_edge(f"{posicion_actual}", f"{movimiento}")
                        mostrar_arbol()

                    if busqueda((nueva_fila, nueva_columna)):
                        return True

        return False

    inicio, meta = encontrar_inicio_meta()
    expansiones = 0
    limite_excedido = False

    if arbol_recibido:
        arbol = arbol_recibido
        nodos = list(arbol.keys())[:-1]
        inicio = obtener_ultimo_nodo(arbol_recibido)
    else:
        arbol = {}
        nodos = []

    movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Arriba, Derecha, Abajo, Izquierda
    grafo = nx.DiGraph()  # Grafo dirigido para visualizar el árbol

    grafo.add_node(f"{inicio}")
    mostrar_arbol()
    busqueda(inicio)
    
    

    return gano


# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [0, 0, 0, 0],
        [0, 1, 1, 3],
        [2, 1, 0, 0],
        [0, 0, 0, 1]
    ]
    arbol_inicial = None  # O un árbol previamente generado
    """
    plt.ion()  # Activar modo interactivo
    arbol_resultante = busqueda_profundidad(matriz, arbol_recibido=arbol_inicial, limite_expansiones=8)
    plt.ioff()  # Desactivar modo interactivo
    plt.show()  # Mostrar el árbol final
    """
    #print(arbol_resultante)
    """
    print("Árbol de búsqueda:")
    for nodo, padre in arbol_resultante.items():
        print(f"{nodo}: {padre}")
    """

    
    
