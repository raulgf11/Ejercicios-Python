#Ejercicio 1: Conversor de temperatura
def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
temperatura_celsius = float(input('Introducir temperatura en grados celsius: '))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f'{temperatura_celsius} grados celsius equivale a {temperatura_fahrenheit} grados fahrenheit')
