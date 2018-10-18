import sys, os, webbrowser
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
  DescentParser(phrase).export_to_file('gram.dot')

# Graphviz - Converter o arquivo .dot gerado em uma imagem PNG
os.system("dot gram.dot -Tpng -o gram.png")

# Abrir o arquivo no Chrome
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("file:///D://dev//compa//gram.png")
