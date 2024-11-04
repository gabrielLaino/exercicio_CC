# Faça um algoritmo recursivo de soma. Esse algoritmo deve receber um número de parâmetro e deve somar todos os números antecessores a ele

def algoritimo_recursivo(n):
  if n <= 1:
    return 1
  else:
    return n * algoritimo_recursivo(n - 1)

print(algoritimo_recursivo(3))
