# -*- coding: utf-8 -*-
from parsing.common import CommonParser
from parsing.elements import ElementoTextual

import sys


class StackParser(CommonParser):
  def __init__(self, phrase):
    super().__init__(phrase)
    self.stack = self._build()


  def _build(self):
    
    stack = []
    
    SINTAGMA_NOMINAL = ['article','adjective','pronoun','noun','proper noun']
    SINTAGMA_VERBAL = ['verb','adverb']
    CONJUNCAO = ['conjunction']
    PREPOSICAO = ['preposition']
    PONTUACAO = ['PUNCTUATION']


    while self._read():
      
      if self._check(SINTAGMA_NOMINAL): 
        stack.append(self.sintagma('NOMINAL', SINTAGMA_NOMINAL,max_len=3))

      elif self._check(SINTAGMA_VERBAL):
        stack.append(self.sintagma('VERBAL', SINTAGMA_VERBAL, max_len=3))

      elif self._check(CONJUNCAO):
        stack.append(self.sintagma('CONJUNCAO', CONJUNCAO,max_len=1))

      elif self._check(PREPOSICAO):
        stack.append(self.sintagma('PREPOSICAO', PREPOSICAO,max_len=1))
      
      elif self._check(PONTUACAO):
        stack.append(ElementoTextual('PONTUACAO',[self._next(),]))

      else:
        self._next()

    return stack


  def sintagma(self, name, partsofspeech, max_len=3):
    termos, temp_len = [], 0

    while self._check(partsofspeech) and temp_len <= max_len:
      termos.append(self._next())
      temp_len += 1
    
    return ElementoTextual(name, termos)
