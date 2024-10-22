# Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para
# ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda".

def retorna_nome_maio (lista):
  nome_maior = ''
  for nome in lista:
    if len(nome) > len(nome_maior):
      nome_maior = nome
  print(nome_maior)

retorna_nome_maio(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])
  