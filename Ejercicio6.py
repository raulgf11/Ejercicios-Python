'''Ejercicio 6: Verificación de Palíndromo Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''
def es_palindromo(palabra):
    if palabra == palabra [::-1]:
      return True
    else:
      return False
palabra = input('Introcuce una pabalabra: ')
if es_palindromo(palabra):
   print(f'La palabra {palabra} es un palíndromo')
else:
   print(f'La palabra {palabra} no es un palíndromo')
