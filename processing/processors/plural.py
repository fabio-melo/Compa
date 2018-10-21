from tokenizer.structure import PartOfSpeech

class PluralTagger:

  def fetch(self, tokens):
    tokens = self.singular_plural(tokens)
    tokens = self.masc_femi(tokens)
    tokens = self.fix_unprocessed(tokens)
    tokens = self.pessoa(tokens)
    return tokens
    
  def singular_plural(self, tokens):
    for x in tokens:
      if isinstance(x.pos,list):
        for y in x.pos:
          if y.grau == 'TEMP':
            try:
              if x.symbol[-1] == 's':
                y.grau = 'plural'
              else:
                y.grau = 'singular'
            except:
              y.grau = 'INDF'
    return tokens

  def masc_femi(self, tokens):
    for x in tokens:
      if isinstance(x.pos,list):
        for y in x.pos:
          if y.genero == 'DESC':
            try:
              if y.grau == 'plural':
                if x.symbol[-2] == 'a':
                  y.genero = 'FEMI'
                elif x.symbol[-2] in ['e', 'o']:
                  y.genero = 'MASC'
              elif y.grau == 'singular':
                if x.symbol[-1] == 'a':
                  y.genero = 'FEMI'
                elif x.symbol[-1] in ['e', 'o']:
                  y.genero = 'MASC'
            except:
              y.genero = 'INDF'
    return tokens

  def pessoa(self, tokens):
    for x in tokens:
      if isinstance(x.pos,list):
        for y in x.pos:
          if y.pessoa == 'DESC':
            if y.tipo in ['noun','proper noun']:
              y.pessoa = 'terceira'
    return tokens



  def fix_unprocessed(self, tokens):
    for x in tokens:
      if isinstance(x.pos, str):
        x.pos = [PartOfSpeech(x.pos,'NONE','NONE')]
    return tokens