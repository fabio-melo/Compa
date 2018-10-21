class ElementoTextual:
  def __init__(self, sintagma, termos):
    self.sintagma = sintagma
    self.termos = termos
    self.grau = ''
    self.genero = ''
    self.pessoa = ''

  def __repr__(self):
    return f'{self.sintagma} {self.termos}'