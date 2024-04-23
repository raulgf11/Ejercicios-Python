'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''
def numeros_pares(lista):
  par = 0
  impar = 0
  for numero in lista:
    if numero % 2 == 0 or numero == 0:
      par += 1
    else:
      impar += 1
  return par , impar

numero = list(map(int, input('Introduzca una lista de numeros separados por espacios: ').split()))
par, impar = numeros_pares(numero)
print(f'Tiene {par} números pares y {impar} número impares')
