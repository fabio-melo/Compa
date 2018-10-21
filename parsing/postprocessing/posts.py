
class PostProcess:

  def sintagma_nominal(self, sintagma):

    if len(sintagma.termos) == 1:
      sintagma.grau = sintagma.termos[0].pos.grau
      sintagma.genero = sintagma.termos[0].pos.genero
      sintagma.pessoa = sintagma.termos[0].pos.pessoa
      return sintagma
    else:
      stack_grau, stack_genero, stack_pessoa = [],[],[]

      for x in sintagma.termos:
        if isinstance(x.pos,list):
          for y in x.pos:
            if y.grau != "DESC": stack_grau.append(y.grau)
            if y.genero != "INDF": stack_genero.append(y.genero)
            if y.pessoa != "INDF": stack_pessoa.append(y.pessoa)
      print(f"{stack_genero} {stack_grau} {stack_pessoa}")

    return sintagma