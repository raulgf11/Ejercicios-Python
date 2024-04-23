'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
def contar_palabras(palabra):
  palabras = palabra.split()
  contador_palabras = len(palabras)
  return contador_palabras
palabra = input('Introduce una frase: ')
numero_palabras = contar_palabras(palabra)
print(f'La frase tiene {numero_palabras} palabras')

