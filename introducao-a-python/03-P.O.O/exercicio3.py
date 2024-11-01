from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
  @abstractmethod
  def area(self):
    raise NotImplementedError
  
  @abstractmethod
  def perimetrio(self):
    raise NotImplementedError
  
class Quadrado(FiguraGeometrica):
  def __init__(self, lado):
    self.lado = lado
  
  def area(self):
    return self.lado * 2
  
  def perimetrio(self):
    return self.lado * 4
  
class Retangulo(FiguraGeometrica):
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  
  def area(self):
    return self.base * self.altura
  
  def perimetrio(self):
    return self.altura * 2 + self.base * 2

retangulo = Retangulo(33, 66)
print(retangulo.area())
print(retangulo.perimetrio())