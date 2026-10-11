def flatten(lista):
    # Caso base: lista vacía
    if not lista:
        return []

    primero, resto = lista[0], lista[1:]

    # Caso recursivo 1: el primero es una sublista, se aplana y se une con el resto
    if isinstance(primero, list):
        return flatten(primero) + flatten(resto)

    # Caso recursivo 2: el primero es un entero, se agrega y se sigue con el resto
    return [primero] + flatten(resto)


# ANÁLISIS BIG-O
# Tiempo:  O(n²) -> los slices y concatenaciones copian listas.
# Espacio: O(n)  -> profundidad de la pila de llamadas.


# === PRUEBAS ===
if __name__ == "__main__":
    print("--- 5. Flatten List ---")
    print(flatten([1, [2, [3, 4], 5]]))   # [1, 2, 3, 4, 5]
    print(flatten([]))                    # []
    