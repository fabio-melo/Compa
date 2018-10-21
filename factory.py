# -*- coding: utf-8 -*-
from tokenizer.extractor import Extractor
from processing.processor import Processor
from spelling.checker import SpellChecker
from spelling.repetition import RepetitionChecker
from parsing.stackparse import StackParser

WORDLISTS = [  
  'wordlists/manual.csv',
  'wordlists/verbosregulares.csv',
  #'wordlists/verbos.csv'
  ]


class CompaFactory():
  def __init__(self):
    self.extractor = Extractor()
    self.processor = Processor(lists=WORDLISTS)
    self.spellcheck = SpellChecker()
    self.repetition = RepetitionChecker()
    
  def execute(self, word):
    # Extrai os Tokens da Frase
    extracted = self.extractor.extract(word)
    # Faz a Checagem Gramatical e retorna os erros encontrados
    errors_spelling = self.spellcheck.from_tokenizer(extracted)
    # Atualiza os tokens extraidos com as correções
    extracted = self.spellcheck.autocorrect(extracted)
    # Atualiza os tokens removendo as duplicadas
    repetitions, extracted =  self.repetition.repetition(extracted)

    # Processa a lista de tokens e adiciona as tags de parte-de-fala
    tagged = self.processor.process(extracted)
    # PARSING


    stack = StackParser(tagged).stack

    for x in stack:
      print(x)

    return errors_spelling, repetitions, stack, tagged