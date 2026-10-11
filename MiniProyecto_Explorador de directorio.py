class ExploradorRecursivo:
    """Clase para explorar y manipular sistemas de archivos simulados mediante diccionarios anidados."""

    def imprimir_arbol(self, sistema: dict, nivel: int = 0) -> None:
        """Muestra la estructura de archivos con indentación visual basada en el nivel recursivo."""
        indentacion = "    " * nivel
        for clave, valor in sistema.items():
            if isinstance(valor, dict):
                # Caso recursivo: es un directorio, imprimimos y bajamos un nivel
                print(f"{indentacion}- {clave}/")
                self.imprimir_arbol(valor, nivel + 1)
            else:
                # Caso base: es un archivo (hoja), se imprime directamente
                print(f"{indentacion}- {clave} ({valor})")

    def buscar_archivo(self, sistema: dict, nombre: str, ruta_actual: str = "") -> str | None:
        """Busca un archivo específico y retorna su ruta relativa dentro del sistema."""
        for clave, valor in sistema.items():
            nueva_ruta = f"{ruta_actual}/{clave}" if ruta_actual else clave
            
            # Caso base 1: Encontramos el archivo buscado en el nivel actual
            if clave == nombre and not isinstance(valor, dict):
                return nueva_ruta
            
            # Caso recursivo: Si es un diccionario (carpeta), buscamos dentro de él
            if isinstance(valor, dict):
                resultado = self.buscar_archivo(valor, nombre, nueva_ruta)
                if resultado is not None:
                    return resultado
                    
        # Caso base 2: Si no se encuentra en esta rama, retorna None
        return None

    def contar_archivos(self, sistema: dict) -> int:
        """Retorna la cantidad total de archivos (las carpetas no cuentan)."""
        total = 0
        for clave, valor in sistema.items():
            if not isinstance(valor, dict):
                # Caso base: Es un archivo (hoja), sumamos 1 al contador
                total += 1
            else:
                # Caso recursivo: Es un directorio, sumamos los archivos de su interior
                total += self.contar_archivos(valor)
        return total


# --- Ejemplo de uso y pruebas ---
if __name__ == "__main__":
    sistema_archivos = {
        "Documentos": {
            "apuntes.txt": "10kb",
            "fotos": {
                "vacaciones.png": "2mb",
                "perro.jpg": "1mb"
            }
        },
        "sistema.dll": "500kb"
    }

    explorador = ExploradorRecursivo()

    print("--- ÁRBOL DE DIRECTORIOS ---")
    explorador.imprimir_arbol(sistema_archivos)

    print("\n--- BÚSQUEDA DE ARCHIVO ---")
    ruta = explorador.buscar_archivo(sistema_archivos, "perro.jpg")
    print(f"Ruta encontrada: {ruta}")

    print("\n--- TOTAL DE ARCHIVOS ---")
    total = explorador.contar_archivos(sistema_archivos)
    print(f"Cantidad total de archivos: {total}")