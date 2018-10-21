from factory import CompaFactory
from parsing.reducer import ReduceParser

compa = CompaFactory()

#x = ['o cara','a mulher','o mulher', 'a rapaz', 'eu', 'tu', 'você', 'o secretária', 'a secretário']

x = ['nós estudamos alegremente']

for y in x:
  _,_, stack, tagged = compa.execute(y)
  ReduceParser(tagged)

#import sys, os, webbrowser

  #DescentParser(phrase).export_to_file('gram.dot') 

# Graphviz - Converter o arquivo .dot gerado em uma imagem PNG
#os.system("dot gram.dot -Tpng -o gram.png")

# Abrir o arquivo no Chrome
#webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("file:///D://dev//compa//gram.png")
