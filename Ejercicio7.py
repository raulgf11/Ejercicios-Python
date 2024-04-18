'''Ejercicio 7: Calculadora Simple Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario. '''

def suma(a, b):
  return a + b
def resta (a, b):
  return a - b
def multiplicacion(a, b):
  return a * b
def division(a, b):
  if b != 0:
    return a / b
  else:
    print('No se puede dividir entre 0')
print('calculadora de operaciones simples: 1. Suma 2. Resta 3. Multiplicacion 4. División')
elegir_calculo = input('Introduce una opción del 1 al 4:')
if elegir_calculo in ('1', '2', '3', '4'):
  a = float(input('Número = '))
  b= float(input('Número = '))
  if elegir_calculo == '1':
    print('Resultado: ', suma(a,b))
  elif elegir_calculo == '2':
    print('Resultado: ', resta(a, b))
  elif elegir_calculo == '3':
    print('Resultado: ', multiplicacion(a, b))
  elif elegir_calculo == '4':
    print('Resultado', division(a , b))
else:
  print('Opción no válida')




    