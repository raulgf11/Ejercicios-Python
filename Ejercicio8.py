'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

def calculo_imc(peso, altura):
  if altura != 0:
    return peso / (altura**2)
  else:
    print('No puedes medir 0 metros')
print('Introduce tu peso en kg y la altura en metros')
peso = float(input('Peso (en kg.): '))
altura = float(input('Altura (en metros): '))
su_imc_es = calculo_imc(peso, altura)
print(f'Su Indice de Masa Corporal es: {su_imc_es}')