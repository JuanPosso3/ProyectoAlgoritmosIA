import random
from busquedaAmplitud import buscar_camino_bfs
from busquedaProfundidad import busqueda_profundidad
from costoUniforme import busqueda_costo_uniforme_con_visualizacion
from profundidadLimitada import buscar_en_laberinto
import matplotlib.pyplot as plt  # Necesario para el modo interactivo de gráficos

# Define una función principal para ejecutar el flujo
def ejecutar_algoritmos():
    # Inicializa las variables necesarias
    matriz = [
        [0, 0, 0, 0],
        [0, 1, 1, 3],
        [2, 1, 0, 0],
        [0, 0, 0, 1]
    ]
    laberinto = matriz  # Para profundidad limitada
    arbol_inicial = None
    mapa_padres = None
    visitados = None
    max_iteraciones = 10  # Un valor predeterminado para evitar bucles infinitos
    algoritmos = ['Amplitud', 'Profundidad', 'costo_uniforme', 'profundidad_limitada']
    ultimo_ejecutado = None

    while algoritmos:
        # Pide al usuario el número de iteraciones o expansiones
        n = int(input("Ingresa el número de iteraciones/expansiones (n): "))

        algoritmo_elegido = random.choice(algoritmos)


        print(f"Ejecutando el algoritmo: {algoritmo_elegido}")

        # Ejecuta el algoritmo elegido
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
        else:
            raise ValueError("Algoritmo desconocido seleccionado.")

        # Comprueba si se encontró solución
        if resultado:  # Suponiendo que los algoritmos devuelven algo evaluable como True si encuentran solución
            print(f"¡Solución encontrada por {algoritmo_elegido}!")
            break

        # Actualiza el último algoritmo ejecutado
        algoritmos.remove(algoritmo_elegido)

    if not algoritmos:
        print("No se encontró solución con ninguno de los algoritmos.")

if __name__ == "__main__":
    ejecutar_algoritmos()
