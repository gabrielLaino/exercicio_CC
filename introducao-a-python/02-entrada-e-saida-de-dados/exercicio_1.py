def nome_invertido():
  nome = input('digite seu nome: ')
  list_nome = list(nome)
  print(nome)
  for i in range(0, len(list_nome)):
    if len(list_nome) > 1:
      list_nome.pop()
      letras = "".join(list_nome)
      print(list_nome)

nome_invertido()