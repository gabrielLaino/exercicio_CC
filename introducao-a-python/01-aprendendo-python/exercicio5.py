# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que
# custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço
# total a partir do tamanho de uma parede (em m²).

import math

def quantidade_latas (tamanho):
  quant_latas = math.ceil(tamanho / 54)
  valor_latas = quant_latas * 80
  print((quant_latas, valor_latas))

quantidade_latas(1000)