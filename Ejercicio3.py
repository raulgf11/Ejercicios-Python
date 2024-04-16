'''Ejercicio 3: Verificación de Edad escribe un programa que solicite la edad de un usuario y determine si es mayor deedad (mayor o igual a 18 años) o no.'''
def verificacion_edad(edad):
  if edad >= 18:
    print('Mayor de edad')
  else:
    print('Menor de edad')
edad = int(input('Ingrese su edad: '))
if edad >= 18:
  print('Es mayor de edad')
else:
  print('Es menor de edad')
