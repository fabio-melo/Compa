from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from collections import deque
from tokenizer import Tokenizer

import sys

# Decorador pra ajudar a debugar
def trace(func):
  def wrapper(self, *args, **kwargs):
    #if self._debug: print(f'Trace: ({self._read().id_}) \
    #  {self._read().symbol} -> {func.__name__} {self._current_level}')
    # \n'f'-> {args[1]}')
    original_result = func(self,*args, **kwargs)
    #print(f'SYN: ({self._read().id_}) {self._read().symbol} -> 
    # (Return) {func.__name__} {self._current_level}')
    #print(f'TRACE: {func.__name__}() ' f'returned {original_result!r}')
    return original_result
  return wrapper


class Grammar:
  def __init__(self, word):
    self.tokens = word
    self.current_token = 0
    self.count = 0
    self.tree = Node('Start')

  def _next(self):
    if self.current_token < len(self.tokens):
      self.current_token += 1
      return self.tokens[self.current_token][1]
    else:
      return False

  def _read(self):
    if self.current_token < len(self.tokens):
      return self.tokens[self.current_token][1]
    else:
      return False

  def _leaf(self,curr):
    tok = self._next()
    return Node(str("("+ str(self.current_token) + ") " + tok[0]), parent=curr)

  def _node(self, curr, msg):
    self.count += 1
    return Node(str(self.count) + ': ' + msg , parent=curr)


  def export_to_file(self,file_):
    self.start()
    with open(file_,'w') as file:
      for x in DotExporter(self.tree):
        file.write(x)


  def _error(self, alert_msg):
    ERRORMSG = '[Syntax] ERROR: Line ' + alert_msg
    print(ERRORMSG)
    return sys.exit()


  def start(self):
    """
    Inicia o Analizador e gera a arvore
    """

    # SINTAGMA NOMINAL
    if self._read() in ['pronoun','article', 'noun']:
      self.sintagma_nominal(self.tree)
      self.sintagma_verbal(self.tree)
    elif self._read() in ['verb', 'adverb']:
      self.sintagma_verbal(self.tree)

    print(RenderTree(self.tree))

  def sintagma_nominal(self, curr):
    
    curr = self._node(curr, "Sintagma Nominal")
    if self._read() in ['pronoun', 'noun']:
      self._next()

  def sintagma_verbal(self, curr):
    pass    


if __name__ == '__main__':
  tk = Tokenizer("eu gosto de maçã").tokens
  Grammar(tk).start()