'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
def es_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, numero):
    if numero % i ==0:
      return False
  else:
    return True
numero = int(input('Introduce un numero entero positivo: '))

if es_primo(numero):
  print(f'El {numero} es primo')
else: 
  print(f'El {numero} No es primo')

