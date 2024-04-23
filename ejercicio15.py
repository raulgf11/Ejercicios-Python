'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
def conversor_tiempo(minutos):
  horas = minutos // 60
  minutos_restantes = minutos % 60
  return horas, minutos_restantes
print('Indicar minutos en el conversor')
minutos = int(input('Minutos: '))
horas,minutos_restantes = conversor_tiempo(minutos)
print(f'{minutos} minutos son {horas} horas y {minutos_restantes} minutos')