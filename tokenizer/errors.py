# -*- coding: utf-8 -*-

class ErrorDetails:
  def __init__(self, tipo, problema, correcao):
    self.tipo = tipo
    self.problema = problema
    self.correcao = correcao

  def __repr__(self):
    return f'{self.tipo}: {self.problema} / {self.correcao}'