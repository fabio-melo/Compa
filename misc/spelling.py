# Carrega as Palavras no Dicionario
import re
from collections import Counter

class Dicionario:

  def __init__(self):
    """ Constrói o dicionário """
    self.dicionario = Counter(re.findall(r'\w+', (open('wordlists/palavras.txt',encoding='utf8').read()).lower()))

  # Funções de edits1 e edits2 de correção, adaptadas do artigo do Peter Norvig, http://norvig.com/spell-correct.html
  def check(self, word): return True if word in self.dicionario else False

  def correction(self, word): 
    print(f"possiveis candidatos: {self.candidates(word)}")
    return max(self.candidates(word))

  def candidates(self,word): return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

  def known(self, words): return set(w for w in words if w in self.dicionario)

  def edits1(self, word):
      letters    = 'abcdefghijklmnopqrstuvwxyzéáíóúâêîôuç'
      splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
      deletes    = [L + R[1:]               for L, R in splits if R]
      transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
      replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
      inserts    = [L + c + R               for L, R in splits for c in letters]
      return set(deletes + transposes + replaces + inserts)

  def edits2(self,word): return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

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
        print(f'grafia incorreta em {s}. você quis dizer {self.candidates(s)} ?')

  def tokenize(self,word):
    return word.rstrip().split()



if __name__ == '__main__':
  d = Dicionario()
  
  print(d.suggest_correction("veio, eu num gosto de pokemon"))
