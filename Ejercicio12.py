'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''

def area_rectangulo(base, altura):
  formula = base * altura
  return formula
print('Introduzca la base y la altura del rectangula en cm. para calcular el área')
base = float(input('La base del rectangulo es: '))
altura= float(input('La altura del rectangulo es: '))
area = area_rectangulo(base,altura)
print(f'El área del rectangulo es {area} cm2')
