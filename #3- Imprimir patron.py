def imprimir_fila(k: int) -> None:
    """Imprime k asteriscos seguidos y un salto de línea."""
    # CASO BASE: ya no quedan asteriscos, se cierra la fila
    if k == 0:
        print()
        return
    # CASO RECURSIVO: imprime uno y sigue con k - 1
    print("*", end="")
    imprimir_fila(k - 1)


def patron(n: int) -> None:
    """Imprime el patrón de 1 hasta n asteriscos, una fila por línea."""
    # CASO BASE: no hay filas que imprimir
    if n <= 0:
        return
    # CASO RECURSIVO: primero las filas anteriores, luego la fila n
    patron(n - 1)
    imprimir_fila(n)


patron(3)
# *
# **
# ***