'''Ejercicio 5: Suma de Números Pares. Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''

def numeros_pares(numero):
  sumar = 0
  for numeros in numero:
    if numeros % 2 == 0:
      sumar += numeros
  return sumar
numero = range(101)
total_pares = numeros_pares(numero)
print('El total de números pares entre el 0 y el 100 son: ', total_pares)


