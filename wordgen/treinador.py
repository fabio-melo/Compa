from nltk.corpus import mac_morpho, floresta
from collections import Counter
import pickle, re

palavras = re.findall(r"[\w'-]+", (open('wordlists/palavras.txt',encoding='utf8').read()).lower())
corpus = list(mac_morpho.words()) + list(floresta.words())
corpus = [x.lower() for x in corpus]

tudo = corpus + palavras

contagem = Counter(tudo)


with open("wordlists/dicionario.bin",'wb') as arq:
  pickle.dump(contagem, arq)