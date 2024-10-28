def soma_valores ():
  valor = input('insira os valores separados por um espaço: ')
  separados = valor.split()
  somados = 0
  for separado in separados:
    if separado.isdigit() :
      somados += int(separado)
    else:
      print('Erro ao somar valores,', separado, 'é um valor invalido') 
  print(somados)

soma_valores()