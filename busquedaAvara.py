import heapq
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

def heuristica(posicion, objetivo):
    """Calcula la heurística h(n) como la distancia de Manhattan."""
    x1, y1 = posicion
    x2, y2 = objetivo
    return abs(x1 - x2) + abs(y1 - y2)

def mostrar_arbol_jerarquico(grafo):
    """Muestra el árbol construido gráficamente en una disposición estrictamente jerárquica."""
    pos = graphviz_layout(grafo, prog="dot")
    plt.clf()
    plt.title("Busqueda avara", fontsize=16)
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

def busqueda_avara(tablero, limite_expansiones):
    """
    Realiza la búsqueda Avara con límite de expansiones y visualización.
    
    Retorna:
        - True si encuentra el objetivo.
        - False si no lo encuentra o alcanza el límite de expansiones.
    """
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

    print(f"Inicio: {inicio}, Objetivo: {objetivo}")

    cola_prioridad = [(heuristica(inicio, objetivo), inicio)]  
    visitados = set()
    grafo = nx.DiGraph() 
    arbol = {}  
    expansiones = 0 

    plt.ion()  

    while cola_prioridad:
        _, actual = heapq.heappop(cola_prioridad)

        
        if actual in visitados:
            continue

        visitados.add(actual)  
        expansiones += 1

        
        nodo_actual = f"({actual[0]},{actual[1]})"
        grafo.add_node(nodo_actual)

        
        if actual in arbol:
            padre = f"({arbol[actual][0]},{arbol[actual][1]})"
            grafo.add_edge(padre, nodo_actual)

        
        mostrar_arbol_jerarquico(grafo)

        
        if expansiones > limite_expansiones:
            print(f"Límite de expansiones alcanzado: {limite_expansiones}")
            plt.ioff()
            plt.show()
            return False

        
        if actual == objetivo:
            print(f"Objetivo encontrado en {actual}.")
            plt.ioff()
            plt.show()
            return True

        
        x, y = actual
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in movimientos:
            nuevo_x, nuevo_y = x + dx, y + dy
            hijo = (nuevo_x, nuevo_y)

            
            if (0 <= nuevo_x < filas and 0 <= nuevo_y < columnas and
                tablero[nuevo_x][nuevo_y] != 1 and hijo not in visitados):

                
                if hijo not in arbol:
                    arbol[hijo] = actual
                heapq.heappush(cola_prioridad, (heuristica(hijo, objetivo), hijo))

    plt.ioff()
    plt.show()
    return False  


if __name__ == "__main__":
    tablero = [
        [0,0,0,0],
        [0,1,1,3],
        [2,1,0,0],
        [0,0,0,1]
    ]

    #limite_expansiones = int(input("Ingrese el límite de expansiones: "))
    #exito = busqueda_avara(tablero, limite_expansiones)
    #print("Resultado de la búsqueda:", "Éxito" if exito else "Falló")
