'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.'''

def final(precio):
  cantidad = precio * 0.80
  return cantidad
print('Introduzca el precio para que le podamos hacer un "20%" de descuento')
precio = float(input('Precio = '))
precio_final = final(precio)
print(f'El precio con descuento es: {precio_final} €')