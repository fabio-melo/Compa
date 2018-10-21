
class PostProcess:

  def fetch(self, tokens):
    tokens = self.single_out('verb', tokens)
    tokens = self.single_out('adverb', tokens)
    return tokens


  def sintagma_nominal(self, sintagma):
    for x in sintagma.termos:
      if isinstance(x.pos,list):
        temp = []
        for y in x.pos:
          if y.tipo == type:
              verbo = True
              temp = y
          if verbo:
            x.pos = [temp,]

    return tokens