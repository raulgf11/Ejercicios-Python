'''Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''

def nacimiento(edad):
  calculo = 2024 - edad
  return calculo
print('Para calcular su edad le pedimos que introduzca su año de nacimiento')
edad = int(input('Año de nacimiento: '))
edad_actual = nacimiento(edad)
print(f'Su edad actual es: {edad_actual}')