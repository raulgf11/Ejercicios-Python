'''Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''
def conversor(millas):
  funcion = millas * 1.60934
  return funcion
print('Introduzca distancia en millas')
millas = float(input('Millas: '))
millas_km = conversor(millas)
print(f'{millas} millas son {millas_km} km.')