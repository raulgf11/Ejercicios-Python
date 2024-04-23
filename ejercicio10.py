'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''

def dia_semana(dia):
  if dia in '1':
    print('Lunes')
  elif dia in '2':
    print('Martes')
  elif dia in '3':
    print('Miercoles')
  elif dia in '4':
    print('Jueves')
  elif dia in '5':
    print('Viernes')
  elif dia in '6':
    print('Sábado')
  elif dia in '7':
    print('domingo')
  return dia
print('Ingrese un número del 1 al 7')
dia = (input('Número: '))
numero = dia_semana(dia)



  
  



