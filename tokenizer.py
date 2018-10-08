# https://www.normaculta.com.br/classes-gramaticais/
from wiktionaryparser import WiktionaryParser
from spelling import Dicionario
import json


class Tokenizer():
  def __init__(self,phrase):
    self.wp = WiktionaryParser()
    self.wp.set_default_language('portuguese')
    self.tokens = self.build_tokens(phrase)



  def build_tokens(self, phrase):
    pr = phrase.rstrip().split()
    things = []
    for x in pr:
      w = self.wp.fetch(x)
      l = [x,]
      try:
        r = w[0]['definitions'][0]['partOfSpeech']
        l.append(r)
      except:
        l.append("none")
      things.append(l)
    print(things)
    return things

        
      
tk = Tokenizer("eu não gosto de banana")

