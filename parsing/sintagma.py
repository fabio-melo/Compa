from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from collections import deque

import sys

# Decorador pra ajudar a debugar
def trace(func):
  def wrapper(self, *args, **kwargs):
    print(f'ENTER: ({self._read().id_}) {self._read().symbol} -> {func.__name__}')
    # \n'f'-> {args[1]}')
    original_result = func(self,*args, **kwargs)
    print(f'EXIT: ({self._read().id_}) {self._read().symbol} -> (Return) {func.__name__} {self._current_level}')
    #print(f'TRACE: {func.__name__}() ' f'returned {original_result!r}')
    return original_result
  return wrapper


class Grammar:

  def __init__(self, phrase):
    self._tokens = phrase
    self._current = 0
    self._count = 0
    self._tree = Node('Start')

  def _next(self):
    """ Retorna a lista de POS de cada token"""
    if self._current < len(self._tokens):
      self._current += 1
      return self._tokens[self._current].pos
    else:
      return False

  def _read(self):
    if self._current < len(self._tokens):
      return self._tokens[self._current].pos
    else:
      return False

  def _leaf(self,curr):
    tok = self._next()
    return Node(f'({self._current}) {tok[0]}', parent=curr)

  def _node(self, curr, msg):
    self._count += 1
    return Node(f'{self._count} : {msg}', parent=curr)

  def export_to_file(self,file_):
    self._start()
    with open(file_,'w') as file:
      for x in DotExporter(self._tree):
        file.write(x)


  def _error(self, alert_msg):
    ERRORMSG = '[Syntax] ERROR: Line ' + alert_msg
    print(ERRORMSG)
    return sys.exit()

  def _pos(self):
    pos = self._read()
    pos_list = []
    for x in pos: pos_list.append(x[0])
    return pos_list


  def _start(self):
    """
    Inicia o Analizador e gera a arvore
    """
    while self._read():
      if not self._read(): break;
      # SINTAGMA NOMINAL
      if self._pos() in ['pronoun','article', 'noun']:
        self.sintagma_nominal(self._tree)
        self.sintagma_verbal(self._tree)
      elif self._pos() in ['verb', 'adverb']:
        self.sintagma_verbal(self._tree)
      else: self._next()

    print(RenderTree(self._tree))

  def sintagma_nominal(self, curr):
    curr = self._node(curr, "Sintagma Nominal")

    if self._pos() in ['pronoun', 'noun']:
      self._next()

  def sintagma_verbal(self, curr):
    curr = self._node(curr, "Sintagma Verbal")
    self._next()

