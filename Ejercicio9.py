'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''
def conversor(dolares):
  return dolares * 0.85
print('Indique la cantidad de dólares que quiere convertir a euros')
dolares = float(input('Dolares: $'))
cambio = conversor(dolares)
print(f'Su cambio a euros es: {cambio}€')