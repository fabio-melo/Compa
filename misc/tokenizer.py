from collections import deque
from wiktionaryparser import WiktionaryParser
import json, re, sys


class Token:
  def __init__(self, symbol, pos, line, id_):
    self.symbol, self.pos = symbol, pos
    self.line, self.id_ = line, id_
  def __str__(self): 
    return f"{self.symbol} {self.pos} {self.line} {self.id_}"

class Lexer:
  def __init__(self, phrase):
    self.tokens, self._current_symbol = [] , []
    self._current_line, self._current_id = 1 , 0
    self._queue = deque(phrase)
    


    self._start()
    self._get_pos()


  def _fetch_next_char(self): 
    return self._queue[0] if self._queue else False


  def _fetch_next_non_blank_char(self):
    while True:
      if not self._queue: 
        return False
      elif re.match(r'[\t\r\f\040]', self._queue[0]): 
        self._queue.popleft()
      elif re.match(r'[\n]',self._queue[0]): 
        self._current_line += 1
        self._queue.popleft()
      else: 
        return self._queue[0]

  def _consume_char(self): 
    if self._queue: self._current_symbol.append(self._queue.popleft())


  def _start(self):
    while self._queue:
      char = self._fetch_next_non_blank_char()

      if not char: break

      elif re.match(r'[a-zA-Z\u00C0-\u00FF]',char): self._identifier()
      elif re.match(r'[0-9]',char): self._number()
      else: 
        self._consume_char()
        self._commit_token('OTHER')

  def _identifier(self):
    while True:
      char = self._fetch_next_char()
      if not char: break
      if re.match('[a-zA-Z\u00C0-\u00FF]', char): 
        self._consume_char()
      else: break
    self._commit_token('TEMP')

  def _number(self):
    while True:
      char = self._fetch_next_char()
      if not char: break
        
      if re.match('[0-9]',char): 
        self._consume_char()
      else: break
     
    self._commit_token('NUMBER')


  def _commit_token(self,code):

    if self._current_symbol:
      temp = ''.join(self._current_symbol)

      self.tokens.append(Token(temp, code, self._current_line,self._current_id))

      self._current_symbol = [] 
      self._current_id += 1

  # POS TAGGING
  def _get_pos(self):
    wp = WiktionaryParser()
    wp.set_default_language('portuguese')

    for x in self.tokens:
      if x.pos == 'TEMP':
        try:
          parts = []
          p = wp.fetch(x.symbol)
          for k in p:
            for y in k['definitions']:
              gender = ''
              if 'm' in y['text'][0].split():
                gender = 'MASC'
              elif 'f' in y['text'][0].split():
                gender = 'FEMI'
              else:
                gender = 'INDF'
              parts.append([y['partOfSpeech'], gender])
          if parts:
            x.pos = parts
          else:
            x.pos = ['desconhecido']
          #x.pos = wp.fetch(x.symbol)[0]['definitions'][0]['partOfSpeech']
        except:
          x.pos = "ERROR"
  


x = Lexer("as coisas nunca são elas").tokens


for y in x:
  print(y)