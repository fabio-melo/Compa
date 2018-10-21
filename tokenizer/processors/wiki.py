# -*- coding: utf-8 -*-
from wiktionaryparser import WiktionaryParser
from tokenizer.structure import PartOfSpeech

class WikiTagger:
  
  def __init__(self):
    self.wp = WiktionaryParser()
    self.wp.set_default_language('portuguese')

  def fetch(self, tokens):
    
    for x in tokens:
      if x.pos == 'TEMP': #or isinstance(x.pos,list):
        try:
          #parts = x.pos if isinstance(x.pos, list) else [] #persistencia
          parts = []
          p = self.wp.fetch(x.symbol)
          for k in p:
            for y in k['definitions']:
              gender = ''
              if 'm' in y['text'][0].split():
                gender = 'MASC'
              elif 'f' in y['text'][0].split():
                gender = 'FEMI'
              else:
                gender = 'INDF'
              coiso = PartOfSpeech(y['partOfSpeech'],gender, "TEMP")
              parts.append(coiso)
          if parts:
            x.pos = parts
          else:
            x.pos = [PartOfSpeech('proper noun','INDF','TEMP'),]
          #x.pos = wp.fetch(x.symbol)[0]['definitions'][0]['partOfSpeech']
        except Exception as e:
          print(e)
          x.pos = "ERROR"
    return tokens