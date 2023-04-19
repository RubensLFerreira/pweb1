import math

numbers = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  numbers.append(num)

for number in numbers:
  if number % 2 == 0:
    print(number)

