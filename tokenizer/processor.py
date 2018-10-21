# -*- coding: utf-8 -*-

from tokenizer.processors.wiki import WikiTagger
from tokenizer.processors.list import ListTagger
from tokenizer.processors.plural import PluralTagger


class Processor:
  def __init__(self, lists=False):
    """ recebe uma lista de caminhos de arquivos .csv """

    if lists:
      self.lt = [ListTagger(x) for x in lists]
    else:
      self.lt = False

    self.wt = WikiTagger()
    self.pt = PluralTagger()

  def process(self, tokens):
    #processamento offline
    if self.lt:
      for x in self.lt:
        tokens = x.fetch(tokens) #pylint: disable=E1111

    #processamento online
    tokens = self.wt.fetch(tokens)
    #plurais
    tokens = self.pt.fetch(tokens)

    return tokens