# -*- coding: utf-8 -*-
# Classe Extrator: extrai os simbolos do texto, para serem tokenizados
import re
from tokenizer.structure import Token

class Extractor:
  def __init__(self):
    #public
    self._tokens = []
    #private
    self._queue = []
    self._c_symbol = []
    self._c_line = 1
    self._c_id = 0
    
    # BUILD
    self._start()
    
  def __str__(self): 
    return f'{self._tokens}'
  def __repr__(self): 
    return f'EXTRACTOR: {self._tokens}'

  def _fetch_next_char(self): 
    return self._queue[-1] if self._queue else False

  def _fetch_next_non_blank_char(self):
    while True:
      if not self._queue: return False
      elif re.match(r'[\t\r\f\040]', self._queue[-1]): self._queue.pop()
      elif re.match(r'[\n]',self._queue[-1]): self._c_line += 1; self._queue.pop()
      else: return self._queue[-1]

  def _consume(self): 
    if self._queue: self._c_symbol.append(self._queue.pop())

  def _start(self):
    while self._queue:
      char = self._fetch_next_non_blank_char()
      if not char: break
      elif re.match(r'[a-zA-Z\u00C0-\u00FFx]',char): self._word()
      elif re.match(r'[0-9]',char): self._number()
      elif re.match(r'[\.\,]',char): self._punctuation()
      else: self._other()

  def _word(self):
    while True:
      char = self._fetch_next_char()
      if not char: break
      if re.match('[a-zA-Z\u00C0-\u00FF]', char): self._consume()
      else: break
    self._commit('TEMP')

  def _number(self):
    while True:
      char = self._fetch_next_char()
      if not char: break
        
      if re.match('[0-9]',char): 
        self._consume()
      else: break
    self._commit('NUMBER')

  def _punctuation(self):
    self._consume()
    self._commit('PUNCTUATION')

  def _other(self):
    self._consume()
    self._commit('OTHER')

  def _commit(self,code):
    if self._c_symbol:
      temp = ''.join(self._c_symbol)
      self._tokens.append(Token(temp, code, self._c_line,self._c_id))
      self._c_symbol = [] 
      self._c_id += 1

  def extract(self, phrase):
    self._tokens = []
    self._queue = list(phrase)[::-1] # lista invertida
    self._c_symbol = []
    self._c_line = 1
    self._c_id = 0
    self._start()
    
    return self._tokens
