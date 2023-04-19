import math

numbers = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  numbers.append(num)

result = 0

for number in numbers:
  result = result + number

print(result)

