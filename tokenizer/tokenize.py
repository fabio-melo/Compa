# -*- coding: utf-8 -*-
from tokenizer.processor import Processor
from tokenizer.extractor import Extractor

class Tokenizer:
  def __init__(self):
    self.proc = Processor()
    self.extr = Extractor()

  def run(self,phrase):
    return self.proc.process(self.extr.extract(phrase))