from tokenizer.processors.wiki import WikiTagger
from tokenizer.processors.list import ListTagger

class Processor:
  def __init__(self):
    self.lt = [ListTagger('tokenizer/wordlists/verbosdefinidos.csv'),]
    self.wt = WikiTagger()

  def run(self, tokens):
    #processamento offline
    if self.lt:
      for x in self.lt:
        tokens = x.fetch(tokens) #pylint: disable=E1111

    #processamento online
    #tokens = self.wt.fetch(tokens)
    return tokens