# -*- coding: utf-8 -*-
from collections import deque

class CommonParser(object):
  """ Funções Comuns de todos os Parsers """
  def __init__(self, phrase):
    self._tokens = deque(phrase)

    
  def _next(self):
    return self._tokens.popleft() if self._tokens else False

  def _read(self):
    return self._tokens[0] if self._tokens else False

  def _error(self, alert_msg):
    print(f'ERROR: {alert_msg}')

  def _check(self,lista):
    if self._read():
      for x in self._read().pos:
        if x.tipo in lista:
          return True
      return False
    else:
      return False