# -*- coding: utf-8 -*-

from processing.processors.wiki import WikiTagger
from processing.processors.list import ListTagger
from processing.processors.plural import PluralTagger
from processing.processors.ambig import AmbiguityTagger

class Processor:
  def __init__(self, lists=False):
    """ recebe uma lista de caminhos de arquivos .csv """

    if lists:
      self.lt = [ListTagger(x) for x in lists]
    else:
      self.lt = False

    self.wt = WikiTagger()
    self.pt = PluralTagger()
    self.at = AmbiguityTagger()


  def process(self, tokens):
    #processamento offline
    if self.lt:
      for x in self.lt:
        tokens = x.fetch(tokens) #pylint: disable=E1111

    #processamento online
    tokens = self.wt.fetch(tokens)
    #plurais
    tokens = self.pt.fetch(tokens)

    tokens = self.at.fetch(tokens)

    return tokens