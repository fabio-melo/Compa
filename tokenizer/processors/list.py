# -*- coding: utf-8 -*-
import csv

class OffDict:
  def __init__(self, file): 
    self.wordlist = self._load(file)

  def __str__(self): return f"{self.wordlist}"

  def _load(self, file):
    with open(file, 'r') as f:
      lista, offlinedict = (list(csv.reader(f))), {}
      for x in lista: 
        if x[0] in offlinedict.keys():
          offlinedict[x[0]].append([[x[1]],x[2],x[3]])
        else:
          offlinedict[x[0]] = [[x[1],x[2],x[3]]]
      return offlinedict

class ListTagger:
  def __init__(self, file_):
    self.o = OffDict(file_)

  def fetch(self, tokens):
    for x in tokens:
      if x.pos == 'TEMP':
        if x.symbol in self.o.wordlist.keys():
          x.pos = self.o.wordlist[x.symbol]
    return tokens
