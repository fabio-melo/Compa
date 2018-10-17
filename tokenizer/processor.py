# -*- coding: utf-8 -*-

from tokenizer.processors.wiki import WikiTagger
from tokenizer.processors.list import ListTagger

class Processor:
  def __init__(self):
    lists = [
      'wordlists/manual.csv',
      'wordlists/verbosregulares.csv',
    ]
    self.lt = [ListTagger(x) for x in lists]
    self.wt = WikiTagger()

  def process(self, tokens):
    #processamento offline
    if self.lt:
      for x in self.lt:
        tokens = x.fetch(tokens) #pylint: disable=E1111

    #processamento online
    tokens = self.wt.fetch(tokens)
    return tokens