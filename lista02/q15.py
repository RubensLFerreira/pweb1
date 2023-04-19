lista = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  lista.append(num)

x = int(input('Digite um número: '))

if x in lista:
  print('O elemento ', x, 'está na lista')
else:
  print('O elemento ', x, 'não está na lista')