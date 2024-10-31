class TV:
  def __init__(self, tamanho):
    self.__tamanho = tamanho
    self.__volume = 50
    self.__canal = 1
    self.__ligado = False

  def __str__(self):
    return f"o tamano da TV é {self.__tamanho}, está no volume {self.__volume} no canal {self.__canal} e está {self.__ligado}"

  def aumenta_volume(self):
    if self.__volume < 99:
      self.__volume += 1
    else:
      print('volume no maximo')
  
  def abaix_volume(self):
    if self.__volume > 0:
      self.__volume -= 1
    else:
      print('volume no minimo')
  
  def muda_canal(self, canal):
    if canal < 1 or canal > 99:
      raise ValueError('canal invalido, deve estra entre 1 e 99')
    else:
      self.__canal = canal
  
  def ligar_desligar(self):
    self.__ligado = not self.__ligado


minha_tv = TV('50')
minha_tv.abaix_volume()
minha_tv.muda_canal(5)
minha_tv.ligar_desligar()
minha_tv.ligar_desligar()
print(minha_tv)


