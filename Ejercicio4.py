'''Ejercicio 4: Contador de Vocales crea un programa que cuente el número de vocales en una palabra ingresada por el usuario'''
def contador_vocales(palabra):
  vocales = 'aeiouAEIOU'
  contador = 0
  for palabras in palabra:
    if palabras in vocales:
      contador += 1
  return contador
palabra = input('Ingrese una palabra: ')
total_vocales = contador_vocales(palabra)
print('Hay',total_vocales,'vocales')
