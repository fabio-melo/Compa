from tokenizer.extractor import Extractor
from tokenizer.processor import Processor
from spelling.checker import SpellChecker

class CompaFactory():
  def __init__(self):
    self.extractor = Extractor()
    self.processor = Processor()
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

    return errors_spelling, tagged
