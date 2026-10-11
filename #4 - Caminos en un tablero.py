def contar_caminos(n, m):
    # Caso base 1: tablero inválido, no hay caminos
    if n <= 0 or m <= 0:
        return 0

    # Caso base 2: con una sola fila o una sola columna hay un único camino
    if n == 1 or m == 1:
        return 1

    # Caso recursivo: caminos si bajo + caminos si voy a la derecha
    return contar_caminos(n - 1, m) + contar_caminos(n, m - 1)


# ANÁLISIS BIG-O
# Tiempo:  O(2^(n+m)) -> cada llamada genera dos más y se repiten subproblemas.
# Espacio: O(n+m)     -> profundidad máxima de la pila de llamadas.


# === PRUEBAS ===
if __name__ == "__main__":
    print("--- 4. Caminos en un Tablero ---")
    print(f"Tablero 2x2: {contar_caminos(2, 2)}")
    print(f"Tablero 3x3: {contar_caminos(3, 3)}")
    print(f"Tablero 3x4: {contar_caminos(4, 4)}")