# -*- coding: utf-8 -*-
from tokenizer.extractor import Extractor
from processing.processor import Processor
from spelling.checker import SpellChecker
from spelling.repetition import RepetitionChecker
from parsing.reducer import ReduceParser

WORDLISTS = [  
  'wordlists/manual.csv',
  'wordlists/verbosregulares.csv',
  #'wordlists/verbos.csv',
  'wordlists/verboest.csv',
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
    spelling_errors = self.spellcheck.from_tokenizer(extracted)
    # Atualiza os tokens extraidos com as correções
    extracted = self.spellcheck.autocorrect(extracted)
    # Atualiza os tokens removendo as duplicadas
    repetitions, extracted =  self.repetition.repetition(extracted)

    # Processa a lista de tokens e adiciona as tags de parte-de-fala
    tagged = self.processor.process(extracted)
    
    # Parser Sintático
    parsed = ReduceParser(tagged)
    semantic_errors = parsed.get_errors()
    reduced = parsed.sintagmas

    #errors = spelling_errors + repetitions + semantic_errors


    return spelling_errors, semantic_errors, repetitions, reduced, tagged, extracted