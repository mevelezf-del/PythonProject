# Programa 2: Ordenar una fila específica de una matriz bidimensional

# Definimos una matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 1, 6],
    [8, 5, 3]
]

# Función para ordenar una fila con Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionamos la fila que queremos ordenar (ejemplo: fila 1)
fila_a_ordenar = 1
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
