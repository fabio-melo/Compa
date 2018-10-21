
class AmbiguityTagger:

  def fetch(self, tokens):
    tokens = self.single_out('verb', tokens)
    tokens = self.single_out('adverb', tokens)
    tokens = self.single_out('pronoun', tokens) 
    tokens = self.single_out('noun', tokens)
    tokens = self.single_out('adjective', tokens)

    return tokens


  def single_out(self, type, tokens):
    for x in tokens:
      if isinstance(x.pos,list):
        temp = []
        verbo = False
        if len(x.pos) > 1:
          for y in x.pos:
            if y.tipo == type:
              verbo = True
              temp = y
          if verbo:
            x.pos = [temp,]

    return tokens