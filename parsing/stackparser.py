# -*- coding: utf-8 -*-

from collections import deque

import sys


class StackParser:

  def __init__(self, phrase):
    self._tokens = deque(phrase)
    self._stack = []

  def _next(self):
    return self._tokens.popleft() if self._tokens else False

  def _read(self):
    return self._tokens[0] if self._tokens else False

  def _error(self, alert_msg):
    ERRORMSG = '[Syntax] ERROR: Line ' + alert_msg
    print(ERRORMSG)


  def _pos(self):
    if self._read():
      pos = self._read().pos
      pos_list = []
      for x in pos: pos_list.append(x[0])
      return pos_list
    else:
      return False

  def _check(self,lista):
    if self._pos():
      for x in self._pos():
        if x in lista:
          return True
      return False
    else:
      return False

  def build(self):
    while self._read():
      if self._check(['article','adjective','pronoun','noun']):
        self._stack.append(self._next())
      else:
        self._stack.append("STOPPER")
        self._next()
    print(self._stack)