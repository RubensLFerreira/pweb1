num = int(input('Digite um número: '))

a, b = 0, 1

while a <= num:
  print('{a} '.format(a = a), end='')
  a, b = b, a + b