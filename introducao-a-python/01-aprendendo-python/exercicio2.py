#Calcule a média aritmética dos valores contidos em uma lista.

def caucula_media (lista):
  valor_itens = 0
  for list in lista:
    valor_itens += list
  media_itens = valor_itens / len(lista)
  return media_itens

print(caucula_media([8, 16, 7, 1]))