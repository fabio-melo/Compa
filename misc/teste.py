# https://www.normaculta.com.br/classes-gramaticais/
from wiktionaryparser import WiktionaryParser
from spelling import Dicionario
import json

wp = WiktionaryParser()
d = Dicionario()
wp.set_default_language('portuguese')

eu = wp.fetch('estamos')
print(eu[0]['definitions'][0])
print(eu[0])
"""
word = "eu"
k = d.tokenize(word)
print(k)

mygrammar = []

for x in k:
  mygrammar.append(wp.fetch(x))

for x in mygrammar:
  try:
    print(x)
  except Exception as e:
    print(e)
    pass
"""