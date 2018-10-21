
class RepetitionChecker:
  def repetition(self, tokens):
    errors, ids =  self.check_for_repetition(tokens)
    tokens = self.remove_repetition(tokens, ids)
    return errors, tokens


  def check_for_repetition(self, tokens):
    errors, ids = [], []
    previous = False
    x = 0
    while x < len(tokens):
      actual = tokens[x].symbol

      if actual == previous:
        errors.append(tokens[x])
        ids.append(tokens[x].id_)
      previous = actual
      x += 1

    return errors, ids

  def remove_repetition(self, tokens, ids):
    return [x for x in tokens if x.id_ not in ids]