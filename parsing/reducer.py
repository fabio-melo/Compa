# -*- coding: utf-8 -*-
from parsing.stackproc import StackProcess
from parsing.stackparse import StackParser

class ReduceParser(StackParser):
  def __init__(self, phrase):
    super().__init__(phrase)
    
    self.errors, self.sintagmas = StackProcess().reduce_elements(self.stack)
    self.print_sintagmas()
    print(self.errors)

  def print_sintagmas(self):
    for x in self.sintagmas:
      print(f'{x.sintagma} {x.grau} {x.genero} {x.pessoa} ', end='\n')