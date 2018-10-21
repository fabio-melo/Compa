from parsing.elements import ElementoTextual

class ReducedSintagma(object):
  def __init__(self, sintagma, genero, grau, pessoa):
    self.sintagma = sintagma
    self.genero = genero
    self.grau = grau
    self.pessoa = pessoa
  def __repr__(self):
    return f"{self.sintagma} ({self.genero}/{self.grau}/{self.pessoa})"



class ShiftReduce:
  def __init__(self, stack):
    self.stack = stack

  def article_noun(self, sintagma):
    # recebe um sintagma nominal
    #'article','adjective','pronoun','noun','proper noun'
    if len(sintagma) == 1:
      a ok
