# -*- coding: utf-8 -*-
from parsing.postparse import PostProcess
from parsing.stackparse import StackParser

class ReduceParser(StackParser):
  def __init__(self, phrase):
    super().__init__(phrase)
    self.post = PostProcess()
    self.errors = []
    self.reduce_elements()
    print(self.stack)
    print(self.errors)

  def reduce_elements(self):
    for element in self.stack:
      if element.sintagma == 'NOMINAL':
        errors, element = self.post.sintagma_nominal(element)
        if errors: self.errors.append(*errors)
      elif element.sintagma == 'VERBAL':
        errors, element = self.post.sintagma_verbal(element)
        if errors: self.errors.append(*errors)
