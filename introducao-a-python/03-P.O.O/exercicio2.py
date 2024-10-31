class Estatistica:
  def __init__(self, numbers):
    self.numbers = numbers
  
  def media(self):
    contador = 0
    for i in self.numbers:
      contador += i
    media_cauculada = contador / len(self.numbers)
    print(f"a media é {media_cauculada}")

  def mediana(self):
    organizado = sorted(self.numbers)
    valor = len(organizado)
    if valor % 2 != 0:
      metade = (valor / 2) - 0.5
      print(f"a mediana e {organizado[int(metade)]}")
    else:
      primeiro = int(valor / 2)
      segundo = primeiro - 1
      valorMediano = (organizado[segundo] + organizado[primeiro]) / 2
      print(f"O valor da mediana é {valorMediano}")



numeros = Estatistica([2, 4, 6, 7, 9, 2, 5, 6])
numeros.mediana()  

