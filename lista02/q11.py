import math

numbers = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  numbers.append(num)

for number in numbers:
  if number % 2 == 1:
    print(number)

