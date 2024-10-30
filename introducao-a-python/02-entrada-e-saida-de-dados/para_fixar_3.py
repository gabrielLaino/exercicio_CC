arquivo = open('file.txt', mode="r")
file = open('escrito.txt', mode="w")

name_list = arquivo.read().split()
list_tupla = []

for name in range(0, len(name_list), 2):
 list_tupla.append((name_list[name], name_list[name + 1]))

for list in list_tupla:
  if int(list[1]) >= 6:
    file.write(f"{list[0]}\n")

arquivo.close()
file.close()