
# Importamos la funcion filtrar_pares
# desde el archivo operaciones.py
from src.operaciones import filtrar_pares

# Creamos una lista de ejemplo
numeros = [1,2,3,4,5]

# Guardamos el resultado de la funcion
resultado = filtrar_pares(numeros)

# Mostramos los numeros pares encontrados
print("Números pares:", resultado)
