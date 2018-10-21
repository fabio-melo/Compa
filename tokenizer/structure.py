# -*- coding: utf-8 -*-

# Classe Tokens: estrutura dos tokens


class Token:
  def __init__(self, symbol, pos, line, id_):
    self.symbol = symbol
    self.pos = pos
    self.line = line
    self.id_ = id_


  def __str__(self): 
    return f"({self.id_}) {self.symbol} {self.pos}"
  def __repr__(self): 
    return f"({self.id_}) {self.symbol} {self.pos}"


class PartOfSpeech:
  def __init__(self, tipo, genero, grau):
    """tipo de parte, genero e grau"""
    self.tipo = tipo
    self.genero = genero
    self.grau = grau
    self.pessoa = 'DESC'


  def __str__(self): 
    return f"{self.tipo}/{self.genero}/{self.grau}/{self.pessoa}"
  def __repr__(self): 
    return f"{self.tipo}/{self.genero}/{self.grau}/{self.pessoa}"

