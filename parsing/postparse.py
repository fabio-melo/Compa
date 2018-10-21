# -*- coding: utf-8 -*-
from parsing.elements import ElementoTextual

def check_unique(elemento): 
  if elemento:
    return all(x==elemento[0] for x in elemento)
  else:
    return True

class PostProcess:

  def sintagma_nominal(self, sintagma):
    errors = []
    stack_grau, stack_genero, stack_pessoa = [],[],[]
    for s in sintagma.termos:
      m_grau, m_genero, m_pessoa = [],[],[]
      for y in s.pos:
        if y.grau != "DESC": m_grau.append(y.grau)
        if y.genero != "DESC": m_genero.append(y.genero)
        if y.pessoa not in ["INDF","DESC"]: m_pessoa.append(y.pessoa)
      if m_grau and check_unique(m_grau): stack_grau.append(m_grau[0])
      #else: stack_grau.append('INDF')
      if m_pessoa and check_unique(m_pessoa): stack_pessoa.append(m_pessoa[0])
      #else: stack_grau.append('INDF')
      if m_genero and check_unique(m_genero): stack_genero.append(m_genero[0])
      #else: stack_grau.append('INDF')

    #REDUZINDO
    if stack_grau and check_unique(stack_grau): sintagma.grau = stack_grau[0]
    else: 
      sintagma.grau = 'INDF'
      errors.append(["Grau", sintagma.termos])

    if stack_pessoa and check_unique(stack_pessoa): sintagma.pessoa = stack_pessoa[0]
    else: 
      sintagma.pessoa = 'INDF'
      errors.append(["Pessoa", sintagma.termos])

    if stack_genero and check_unique(stack_genero): sintagma.genero = stack_genero[0]
    else: 
      test = [x for x in stack_genero if x != "INDF"]
      sintagma.genero = 'INDF'
      if test and not check_unique(test):
        errors.append(["Genero", sintagma.termos])
    #print(f"{stack_genero} \n {stack_grau} \n {stack_pessoa}")
    #print(errors)
    return errors,sintagma

  def sintagma_verbal(self, sintagma):
    errors = []
    stack_grau, stack_pessoa = [],[]

    for termo in sintagma.termos:
      m_grau, m_pessoa = [],[]
      for y in termo.pos:
        if y.tipo == 'verb':
          if y.grau != "DESC": m_grau.append(y.grau)
          if y.pessoa not in ["INDF","DESC"]: m_pessoa.append(y.pessoa)
        if m_grau and check_unique(m_grau): stack_grau.append(m_grau[0])
        #else: stack_grau.append('INDF')
        if m_pessoa and check_unique(m_pessoa): stack_pessoa.append(m_pessoa[0])
        #else: stack_grau.append('INDF')
    
    #REDUZINDO
    if stack_grau and check_unique(stack_grau): sintagma.grau = stack_grau[0]
    else: 
      sintagma.grau = 'INDF'
      errors.append(["Grau", sintagma.termos])

    if stack_pessoa and check_unique(stack_pessoa): sintagma.pessoa = stack_pessoa[0]
    else: 
      sintagma.pessoa = 'INDF'
      errors.append(["Pessoa", sintagma.termos])
    
    #print(f"VERBO {stack_grau} \n {stack_pessoa}")
    return errors, sintagma
