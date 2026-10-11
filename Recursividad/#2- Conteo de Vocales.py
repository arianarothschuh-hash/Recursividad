#2- Conteo de Vocales.
def contar_vocales(s,indice=0):
    if indice == len(s):
        return 0
    vocales = "aeiouAEIOU"
    es_vocal = 1 if s[indice] in vocales else 0
    return es_vocal + contar_vocales(s, indice + 1)

#Ejemplo de uso
print (contar_vocales("Hola Mundo"))  # Salida: 4
print (contar_vocales("Recursividad"))  # Salida: 5
print (contar_vocales("Montaña")) # Salida: 3
print (contar_vocales("Computadora")) # Salida: 5
print (contar_vocales("Vocabulario")) # Salida: 6
print (contar_vocales("ESTUDIANTE")) # Salida: 5