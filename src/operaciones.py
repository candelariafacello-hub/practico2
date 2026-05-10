
def filtrar_pares(lista):
 # Lista vacia donde vamos a guardar
    # los numeros pares encontrados
  pares = []

 # Recorremos cada numero de la lista
  for numero in lista:
  
# Verificamos si el numero es par
       # usando el operador modulo (%)
    if numero % 2 == 0:
      # Si es par, lo agregamos a la lista
      pares.append(numero)

 # Devolvemos la lista de numeros pares
  return pares
