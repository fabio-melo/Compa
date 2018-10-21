class Splitter:

  def split(self, tokens):
    phrases = []
    building = []
    while tokens:
      if tokens[0] == 'PUNCTIONATION':
        tokens.popleft()
        if building:
          phrases.append(building)
          building = []
      else:
        building.append(tokens.popleft())
    return list(tokens)

