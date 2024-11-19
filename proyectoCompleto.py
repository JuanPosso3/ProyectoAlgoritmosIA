import random
from busquedaAmplitud import buscar_camino_bfs
from busquedaProfundidad import busqueda_profundidad
from costoUniforme import busqueda_costo_uniforme_con_visualizacion
from profundidadLimitada import buscar_en_laberinto
from profundidadIterativa import ejecutar_busqueda
from busquedaAvara import busqueda_avara
import matplotlib.pyplot as plt  

def ejecutar_algoritmos():
    
    matriz = [
        [0, 0, 0, 0],
        [0, 1, 1, 3],
        [2, 1, 0, 0],
        [0, 0, 0, 1]
    ]
    laberinto = matriz  
    arbol_inicial = None
    mapa_padres = None
    visitados = None
    max_iteraciones = 10  
    algoritmos = ['Amplitud', 'Profundidad', 'costo_uniforme', 'profundidad_limitada','profundidad_iterativa', 'Avara']
    ultimo_ejecutado = None

    while algoritmos:
        n = int(input("Ingresa el número de iteraciones/expansiones (n): "))

        algoritmo_elegido = random.choice(algoritmos)


        print(f"Ejecutando el algoritmo: {algoritmo_elegido}")

        
        if algoritmo_elegido == 'Amplitud':
            resultado = buscar_camino_bfs(matriz, n)
        elif algoritmo_elegido == 'Profundidad':
            plt.ion()  
            resultado = busqueda_profundidad(matriz, arbol_recibido=arbol_inicial, limite_expansiones=n)
            plt.ioff()  
            plt.show()
        elif algoritmo_elegido == 'costo_uniforme':
            resultado = busqueda_costo_uniforme_con_visualizacion(matriz, mapa_padres, visitados, max_iteraciones=n)
        elif algoritmo_elegido == 'profundidad_limitada':
            resultado = buscar_en_laberinto(laberinto, n)
        elif algoritmo_elegido == 'profundidad_iterativa':
            resultado = ejecutar_busqueda(matriz, n)
        elif algoritmo_elegido == 'Avara':
            resultado = busqueda_avara(matriz,n)
        else:
            raise ValueError("Algoritmo desconocido seleccionado.")

        
        if resultado:  
            print(f"¡Solución encontrada por {algoritmo_elegido}!")
            break

        
        algoritmos.remove(algoritmo_elegido)

    if not algoritmos:
        print("No se encontró solución con ninguno de los algoritmos.")

if __name__ == "__main__":
    ejecutar_algoritmos()
