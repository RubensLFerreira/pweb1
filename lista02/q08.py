# from math import max, min
import math

numbers = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  numbers.append(num)
    
print(
  'Número máximo', max(numbers),
  'Número minimo', min(numbers)
  )