from parsing.common import CommonParser
from tokenizer.structure import Token
class RepetitionParser(CommonParser):
  def __init__(self, phrase):
    super().__init__(phrase)
    self.errors = self.check_for_repetition()
    
  def check_for_repetition(self):
    errors = []
    previous = Token(None,None,None, None)
    while self._read():
      actual = self._next()
      if actual.symbol == previous.symbol:
        errors.append(actual.symbol)
      previous = actual
    return errors