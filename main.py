import sys, os
from tokenizer.extractor import Extractor
from tokenizer.processor import Processor
from parsing.descent import DescentParser
#import misc.geradores.verbos_reg

if __name__ == '__main__':
  pr = Processor()
  ex = Extractor()

  phrase = pr.process(ex.extract(sys.argv[1]))

  for y in phrase:
    print(y)
  DescentParser(phrase)._start()
