# -*- coding: utf-8 -*-

# Classe Tokens: estrutura dos tokens


class Token:
  def __init__(self, symbol, pos, line, id_):
    self.symbol = symbol
    self.pos = pos
    self.line = line
    self.id_ = id_


  def __str__(self): 
    return f"{self.symbol} {self.pos} {self.line} {self.id_}"
  def __repr__(self): 
    return f"{self.symbol} {self.pos} {self.line} {self.id_}"
