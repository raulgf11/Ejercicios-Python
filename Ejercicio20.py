'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.'''

def suma_lista(numero):
  suma = 0
  for numeros in numero:
    suma += numeros
  return suma
numero = list(map(int, input('Introduce una lista de números separados por espacios: ').split()))
suma_numeros = suma_lista(numero)
print(f'{suma_numeros} es la suma de los números que has introducido')