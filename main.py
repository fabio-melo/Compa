from factory import CompaFactory
from parsing.stackparser import StackParser

from parsing.postprocess import PostProcess

compa = CompaFactory()

#x = ['o cara','a mulher','o mulher', 'a rapaz', 'eu', 'tu', 'você', 'o secretária', 'a secretário']

x = ['os muleque','os muleques']

for y in x:
  _,_, stack = compa.execute(y)
  print(y)
  d = PostProcess(stack)
  d.sintagma_nominal(stack[0])

#import sys, os, webbrowser

  #DescentParser(phrase).export_to_file('gram.dot') 

# Graphviz - Converter o arquivo .dot gerado em uma imagem PNG
#os.system("dot gram.dot -Tpng -o gram.png")

# Abrir o arquivo no Chrome
#webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("file:///D://dev//compa//gram.png")
