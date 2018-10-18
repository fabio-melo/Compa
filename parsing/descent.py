# -*- coding: utf-8 -*-

from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from collections import deque

import sys

# Decorador pra ajudar a debugar
def trace(func):
  def wrapper(self, *args, **kwargs):
    print(f'ENTER: -> {func.__name__} - {self._read()} ')
    # \n'f'-> {args[1]}')
    original_result = func(self,*args, **kwargs)
    print(f'EXIT: -> (Return) {func.__name__}')
    #print(f'TRACE: {func.__name__}() ' f'returned {original_result!r}')
    return original_result
  return wrapper


class DescentParser:

  def __init__(self, phrase):
    self._tokens = deque(phrase)
    self._current = 0
    self._count = 0
    self._tree = Node('Sintagma')

  def _next(self):
    """ Retorna a lista de POS de cada token"""
    if self._tokens:
      self._current += 1
      return self._tokens.popleft()
    else:
      return False

  def _read(self):
    if self._tokens:
      return self._tokens[0]
    else:
      return False

  def _leaf(self,curr):
    tok = self._next()
    return Node(f'({self._current}) {tok.symbol}', parent=curr)

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

  @trace
  def _start(self):
    """
    Inicia o Analizador e gera a arvore
    """
    print(self._pos())
    if self._check(['pronoun', 'article']):
      self._SN(self._tree)
    elif self._check(['proper noun','noun','adjective']):
      self._SA(self._tree)
    elif self._check(['adverb','verb']):
      self._SV(self._tree)
    elif self._check(['conjunction','preposition']):
      self._SC(self._tree)
    
    #print(RenderTree(self._tree))
  @trace
  def _SN(self, curr):
    curr = self._node(curr, "Sintagma Nominal")

    if self._check(['article']):
      token = self._read().symbol
      self._leaf(curr)
      if self._check(['noun', 'proper noun','adjective']):
        pass
      else:
        self._error(f"Possível Erro: Faltando Substantivo depois do Artigo {token}")

    elif self._check(['pronoun']): 
      self._leaf(curr)


    # TRANSIÇÃO 
    if self._check(['adjective','noun', 'proper noun']):
      self._SA(curr) # transição

    elif self._check(['conjunction', 'preposition']):
      self._SC(curr) # transição

    elif self._check(['adverb','verb']):
      self._SV(curr)

  @trace
  def _SA(self,curr):
    curr = self._node(curr, "Adjetivo/Substantivo")
    self._leaf(curr)
    if self._check(['noun', 'proper noun']):
      self._leaf(curr)
      if self._check(['adjective']):
        self._leaf(curr)
    elif self._check(['adjective']):
      self._leaf(curr)
      if self._check(['noun', 'proper noun']):
        self._leaf(curr)

    if self._check(['conjunction', 'preposition']):
      self._SC(curr) # transição
    elif self._check(['adverb','verb']):
      self._SV(curr)
    
  @trace
  def _SC(self, curr):
    curr = self._node(curr, "Conjunção Preposição")
    self._leaf(curr)

    # TRANSIÇÃO
    if self._check(['conjunction', 'preposition']):
      self._SC(curr) # transição
    elif self._check(['pronoun', 'article']):
      self._SN(curr)
    elif self._check(['adverb','verb']):
      self._SV(curr)
    elif self._check(['adjective', 'noun', 'proper noun']):
      self._SA(curr) # transição




  @trace
  def _SV(self, curr):
    curr = self._node(curr, "Sintagma Verbal")
    
    if self._check(['verb','adverb']):
      self._leaf(curr)
      if self._check(['verb','adverb']):
        self._leaf(curr)
        if self._check(['verb','adverb']):
          self._error("Demasiados Verbos/Advérbios seguidos")
    
    if self._check(['pronoun', 'article']):
      self._SN(curr)
    elif self._check(['conjunction','preposition']):
      self._SC(curr)
    elif self._check(['adjective', 'noun', 'proper noun']):
      self._SA(curr) # transição

