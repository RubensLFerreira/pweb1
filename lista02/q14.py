lista = []

for i in range(1, 11):
  num = int(input('Digite um número: '))
  lista.append(num)

decrescente = sorted(lista, reverse=True)

print(decrescente)