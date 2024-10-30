import json

with open('valores.json') as file:
    constend = file.read()
    linguagens = json.loads(constend)

palvras = []

for i in linguagens:
    for categorias in i['categories']:
        for palavra in palvras:
            if palavra["categoria"] == categorias:
                palavra["contagem"] += 1
                break
        else:
            palvras.append({"categoria": categorias, "contagem": 1})

print(palvras)
