#Dada uma lista, descubra o menor elemento. Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2

def menor_numero (lista):
  menor = 10000000000000000000000
  for elemento in lista:
    if elemento < menor:
      menor = elemento
  return menor

print(menor_numero([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))