from tokenizer.extractor import Extractor
from tokenizer.splitter import Splitter
from processing.processor import Processor
from spelling.checker import SpellChecker
from parsing.repetition import RepetitionParser
from parsing.stackparser import StackParser

WORDLISTS = [  
  'wordlists/manual.csv',
  'wordlists/verbosregulares.csv',]


class CompaFactory():
  def __init__(self):
    self.extractor = Extractor()
    self.splitter = Splitter()
    self.processor = Processor(lists=WORDLISTS)
    self.spellcheck = SpellChecker()
    
  def execute(self, word):
    # Extrai os Tokens da Frase
    extracted = self.extractor.extract(word)
    # Faz a Checagem Gramatical e retorna os erros encontrados
    errors_spelling = self.spellcheck.from_tokenizer(extracted)
    # Atualiza os tokens extraidos com as correções
    extracted = self.spellcheck.autocorrect(extracted)
    # Processa a lista de tokens e adiciona as tags de parte-de-fala
    tagged = self.processor.process(extracted)
    # Verifica a pontuação e separa a frase
    #phrases = self.splitter.split(tagged)
    # PARSING
    
    repetitions = RepetitionParser(tagged).errors
    stack = StackParser(tagged)._tokens
    
    print(repetitions)


    return errors_spelling, tagged
