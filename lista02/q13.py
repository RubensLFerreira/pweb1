lista = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  lista.append(num)

crescente = sorted(lista)

print(crescente)