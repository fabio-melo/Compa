# -*- coding: utf-8 -*-
# Carrega as Palavras no Dicionario
import re, pickle
from collections import Counter

class SpellChecker:

  def __init__(self, trained=True):
    """ Constrói o spellchecker """
    self.dicionario = []
    self.qtd = None
    if trained: 
      self.load_trained_data()
    else:
      self.dicionario = Counter(re.findall(r"[\w'-]+", (open('wordlists/palavras.txt',encoding='utf8').read()).lower()))
      self.qtd = len(self.dicionario)
      print(f"Dicionario Carregado - sem processamento - numero de palavras: {self.qtd}, numero de entradas: {len(self.dicionario)}")

  def load_trained_data(self):
    with open('wordlists/dicionario.bin','rb') as d:
      self.dicionario = pickle.load(d)
      self.qtd = sum(self.dicionario.values())
      print(f"Dicionário Carregado - numero de palavras: {self.qtd}, numero de entradas: {len(self.dicionario)}")


  # Funções de edits1 e edits2 de correção, adaptadas do artigo do Peter Norvig, http://norvig.com/spell-correct.html
  def check(self, word): 
    return True if word in self.dicionario else False

  def correction(self, word): 
    #print(f"possiveis candidatos: {self.candidates(word)}")
    return max(self.candidates(word), key=self.prob)

  def prob(self, word): 
    return self.dicionario[word] / self.qtd

  def candidates(self,word): 
    return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

  def known(self, words): 
    return set(w for w in words if w in self.dicionario)

  def edits1(self, word):
      letters    = 'abcdefghijklmnopqrstuvwxyzéáíóúâêîôuç'
      splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
      deletes    = [L + R[1:]               for L, R in splits if R]
      transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
      replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
      inserts    = [L + c + R               for L, R in splits for c in letters]
      return set(deletes + transposes + replaces + inserts)

  def edits2(self,word):
    return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

  # checagem de frases
  def check_phrase(self, sentence):
    sentence, bad_words = re.sub(r'[^\w\s\,]',' ',sentence).lower().split(), []
    print(sentence)
     
    for x in sentence: 
      if not self.check(x): bad_words.append(x)
    
    return bad_words
  
  def suggest_correction(self, sentence):
    checked = self.check_phrase(sentence)
    if checked:
      for s in checked:
        print(f'grafia incorreta em {s}. você quis dizer {self.correction(s)} ?')


  def from_tokenizer(self, tokens):
    bad_words = []

    for x in tokens:
      """lê dos tokens e informa dos erros ao usuario"""
      tok = []
      if not self.check(x.symbol):
        tok.append(x.symbol)
        corrected = self.correction(x.symbol)
        if x.symbol == corrected:
          tok.append(False)
        else:
          tok.append(self.correction(x.symbol))
        bad_words.append(tok)
    return bad_words

  def autocorrect(self, tokens):
    """corrige in place e retorna a lista de tokens corrigidos"""
    for x in tokens:
      if not self.check(x.symbol):
        x.symbol = self.correction(x.symbol)
    return tokens


