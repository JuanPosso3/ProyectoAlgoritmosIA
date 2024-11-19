import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import heapq


def busqueda_costo_uniforme_con_visualizacion(matriz, mapa_padres, visitados, max_iteraciones):
    filas, columnas = len(matriz), len(matriz[0])
    inicio, objetivo = None, None
    contador_iteraciones = 0
    gano=False

    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] == 2:
                inicio = (fila, columna)
            elif matriz[fila][columna] == 3:
                objetivo = (fila, columna)

    if not inicio or not objetivo:
        return "Inicio o objetivo no definidos en la matriz", mapa_padres

    grafo = nx.DiGraph()

    def eliminar_nodos_antiguos(visitados):
        if len(visitados) <= 2:
            return set()
        lista_visitados = list(visitados)
        return set(lista_visitados[2:])

    if visitados is not None:
        visitados = eliminar_nodos_antiguos(visitados)

    if mapa_padres is None:
        mapa_padres = {inicio: None}
    if visitados is None:
        visitados = set()

    def configurar_cola_prioridad(mapa_padres):
        todos_nodos = set(mapa_padres.keys())
        nodos_hijos = set(mapa_padres.values()) - {None}
        nodos_hoja = todos_nodos - nodos_hijos

        cola_prioridad = []
        for nodo in nodos_hoja:
            costo = calcular_costo(nodo, mapa_padres)
            cola_prioridad.append((costo, nodo))

        heapq.heapify(cola_prioridad)
        return cola_prioridad

    def calcular_costo(nodo, mapa_padres):
        costo = 0
        actual = nodo
        while mapa_padres[actual] is not None:
            costo += 1
            actual = mapa_padres[actual]
        return costo

    def reconstruir_camino(mapa_padres, inicio, objetivo):
        camino = []
        pasos = []
        actual = objetivo
        while actual:
            camino.append(actual)
            actual = mapa_padres[actual]
        camino.reverse()

        for i in range(len(camino) - 1):
            pasos.append((camino[i], camino[i + 1]))

        return gano

    def obtener_vecinos(posicion, filas, columnas):
        fila, columna = posicion
        vecinos = []
        for desplazamiento_fila, desplazamiento_columna in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nueva_fila, nueva_columna = fila + desplazamiento_fila, columna + desplazamiento_columna
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                vecinos.append((nueva_fila, nueva_columna))
        return vecinos

    def mostrar_arbol_jerarquico(grafo):
        
        pos = graphviz_layout(grafo, prog="dot")
        plt.clf()
        plt.title("Algoritmo costo uniforme", fontsize=16)
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

    cola_prioridad = configurar_cola_prioridad(mapa_padres)


    plt.ion()

    while cola_prioridad and contador_iteraciones < max_iteraciones:
        costo, actual = heapq.heappop(cola_prioridad)
        if actual in visitados:
            continue
        visitados.add(actual)
        contador_iteraciones += 1

        
        if actual not in grafo:
            grafo.add_node(str(actual))
        if mapa_padres[actual] is not None:
            grafo.add_edge(str(mapa_padres[actual]), str(actual))

        mostrar_arbol_jerarquico(grafo)

        
        if actual == objetivo:
            gano=True
            plt.ioff()
            mostrar_arbol_jerarquico(grafo)
            plt.show()
            return reconstruir_camino(mapa_padres, inicio, objetivo)

        
        for vecino in obtener_vecinos(actual, filas, columnas):
            if vecino not in visitados and matriz[vecino[0]][vecino[1]] != 1:
                heapq.heappush(cola_prioridad, (costo + 1, vecino))
                if vecino not in mapa_padres:
                    mapa_padres[vecino] = actual

    plt.ioff()
    plt.show()
    return gano 

if __name__ == "__main__":
    
    """
    matriz = [
        [0,0,0,0],
        [0,1,1,3],
        [2,1,0,0],
        [0,0,0,1]
    ]

    mapa_padres=None
    """

    """
    prueba
    mapa_padres ={
        (0, 0) : None,
        (1, 0) : (0, 0),
        (2, 0) : (1, 0),
        (3, 0) : (2, 0),
        (3, 1) : (3, 0),
        (3, 2) : (3, 1),
        (2, 2) : (3, 2),
        (3, 3) : (3, 2) 
    }
    """


    #visitados = None
    #max_iteraciones = 3

    
    #pasos = busqueda_costo_uniforme_con_visualizacion(matriz, mapa_padres, visitados, max_iteraciones)
    #print(pasos)
    """
    if pasos:
        print("\nPasos encontrados:")
        for paso in pasos:
            print(f"Mover de {paso[0]} a {paso[1]}")
    else:
        print("\nNo se encontró un camino en el número máximo de iteraciones.")
        for nodo, padre in mapa_padres_final.items():
            print(f"{padre} -> {nodo}")
            """
