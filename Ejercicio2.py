'''Ejercicio 2: Calculadora de Propina Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.'''

def total(cantidad):
  cuenta_total = cantidad * 1.15
  return cuenta_total
cantidad=float(input('Introducir cantidad sin propina: '))
con_propina = total(cantidad)
print(f'La cuenta total es de: {con_propina}')


  
