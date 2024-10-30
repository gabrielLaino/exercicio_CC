import random

arquivo = open('palavras.txt')
letor = arquivo.read().split()
palavra = random.choice(letor)
palavra_embaralhada = "".join(random.sample(palavra, len(palavra)))
print('Bem vindo ao jogo das palavras da Larissa')
print(f"A palavra embaralhada e {palavra_embaralhada}")
tentativa = input('Qual a sua tentativa: ')
if tentativa == palavra:
  print('você ganhou um beijo')
else:
  print('perdeu lava a loça')
arquivo.close()