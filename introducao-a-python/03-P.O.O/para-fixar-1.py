class ventilador:
  def __init__(self, cor, potencia, tensao, preco):
    self.cor = cor
    self.potencia = potencia
    self.tensao = tensao
    self.preco = preco
  
  def __str__(self):
    return f"Ventilado {self.cor}, {self.preco}"

meu_ventilador = ventilador('vermelho', '1000', '100', 'R$ 50,00')
print(meu_ventilador)