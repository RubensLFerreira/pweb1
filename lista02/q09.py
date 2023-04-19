import math

numbers = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  numbers.append(num)

print('A média é', sum(numbers), 'e a média é', sum(numbers) / len(numbers))