# -*- coding: utf-8 -*-
from parsing.stackproc import StackProcess
from parsing.stackparse import StackParser
from parsing.elements import ElementoTextual
from tokenizer.errors import ErrorDetails

class ReduceParser(StackParser):
  def __init__(self, phrase):
    super().__init__(phrase)

    self.errors, self.sintagmas = StackProcess().reduce_elements(self.stack)
    #self.print_sintagmas()
    self.reduce()
    #print(self.errors)
  def get_errors(self):
    return self.errors

  def print_sintagmas(self):
    for x in self.sintagmas:
      print(f'{x.sintagma} {x.grau} {x.genero} {x.pessoa} ', end='\n')


  def reduce(self):
    it = 0
    while it < len(self.sintagmas):

      sin1 = self.sintagmas[it]   if it   < len(self.sintagmas) else ElementoTextual(False,False)
      sin2 = self.sintagmas[it+1] if it+1 < len(self.sintagmas) else ElementoTextual(False,False)

      # SUJEITO E VERBO
      if sin1.sintagma == "NOMINAL" and sin2.sintagma == "VERBAL":
        if sin1.grau == sin2.grau: pass #print("ok GRAU")
        else: 
          self.errors.append(ErrorDetails("SN_SV_GRAU", sin1.termos + sin2.termos, None))
        if sin1.pessoa == sin2.pessoa: pass #print("OK PESSOA")
        else: 
          self.errors.append(ErrorDetails("SN_SV_PESSOA", sin1.termos + sin2.termos, None))
        it += 2
      else:
        it += 1

