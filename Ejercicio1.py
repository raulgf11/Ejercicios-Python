#Ejercicio 1: Conversor de temperatura
def conversor_temperatura(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
celsius = float(input('Introducir temperatura en grados celsius: '))
temperatura_fahrenheit = conversor_temperatura(celsius)
print(f'La temperatura en fahrenheit son: {temperatura_fahrenheit} ')
