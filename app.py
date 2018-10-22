from flask import Flask, render_template, request, flash
import subprocess
from factory import CompaFactory
from tokenizer.errors import ErrorDetails

app = Flask(__name__)
app.secret_key = 'development key'

cf = CompaFactory()

@app.route('/', methods=['GET','POST'])
def start_server():
  if request.method == 'POST':
    print(request.form['Text1'])
    
    texto = request.form['Text1']
    spelling, semantic, repetitions, reduced, tagged, extracted\
    = cf.execute(request.form['Text1'].lower())

    colortext = gerar_colorizacao(reduced)

    voice, errors = errors_to_spoken_string(spelling, repetitions, semantic)

    return render_template('index.html', texto=texto, spelling=spelling, \
    semantic=semantic, repetitions=repetitions, reduced=reduced, tagged=tagged, \
    extracted=extracted, voice=voice,errors=errors, colortext=colortext)
  else:
    return render_template('index.html')

def errors_to_spoken_string(spelling, repetitions, semantic):
  voice, html = [], []
  for x in spelling:
    if isinstance(x, ErrorDetails):
      #print(x.problema)
      a = " ".join(x.problema)
      b = " ".join(x.correcao)
      voice.append(f"Grafia Incorreta na Palavra { a }, você quis dizer { b }?")

      html.append(f'Grafia incorreta na palavra "<b>{x.problema}</b>", você quis dizer "<b>{x.correcao}</b>"?')

  for x in repetitions:
    print(repetitions)
    voice.append(f"Repetição encontrada na palavra {x.problema}")
    html.append(f"Repetição encontrada na palavra <b>{x.problema}</b>")

  for x in semantic:
    palavra = []
    for y in x.problema:
      palavra.append(y.symbol)

    palavra = " ".join(palavra)

    if x.tipo == 'SN_SV_GRAU':
      voice.append(f"Erro de concordância de Grau entre sujeito e verbo na sentença {palavra}.")
      html.append(f"Erro de concordância de <b>Grau</b> entre sujeito e verbo em '<b>{palavra}</b>'.")

    elif x.tipo == 'SN_SV_PESSOA':
      voice.append(f"Erro de concordância de pessoa verbal entre sujeito e verbo na sentença {palavra}.")
      html.append(f"Erro de concordância de <b>Pessoa</b> entre sujeito e verbo em '<b>{palavra}</b>'.")

    elif x.tipo == 'SN_GENERO':
      voice.append(f"Erro de concordância de gênero no sintagma nominal {palavra}.")
      html.append(f"Erro de concordância de <b>Gênero</b> no sintagma nominal <b>{palavra}</b>.")

    elif x.tipo == 'SN_GRAU':
      voice.append(f"Erro de concordância de grau no sintagma nominal {palavra}.")
      html.append(f"Erro de concordância de <b>Grau</b> no sintagma nominal <b>{palavra}</b>.")

    elif x.tipo == 'SV_GRAU':
      voice.append(f"Erro de concordância de grau no sintagma verbal {palavra}.")
      html.append(f"Erro de concordância de <b>Grau</b> no sintagma verbal <b>{palavra}</b>.")

    elif x.tipo == 'SV_PESSOA':
      voice.append(f"Erro de concordância de Pessoa no sintagma verbal {palavra}.")
      html.append(f"Erro de concordância de <b>Pessoa</b> no sintagma verbal <b>{palavra}</b>.")
  
  voice = ".".join(voice)
  print(voice)
  return voice, html

def gerar_colorizacao(reduced):
  stringue = []
  for x in reduced:
    if x.sintagma == "NOMINAL":
      mini = []
      for y in x.termos:
        mini.append(y.symbol)
      mini = " ".join(mini)
      mini = f"<mark class='bg-primary text-white'>{mini}</mark>" 
      stringue.append(mini)
    if x.sintagma == "VERBAL":
      mini = []
      for y in x.termos:
        mini.append(y.symbol)
      mini = " ".join(mini)
      mini = f"<mark class='bg-success text-white'>{mini}</mark>" 
      stringue.append(mini)
    if x.sintagma in ["CONJUNCAO","PREPOSICAO","PONTUACAO"]:
      mini = []
      for y in x.termos:
        mini.append(y.symbol)
      mini = " ".join(mini)
      mini = f"<mark class='bg-danger text-white'>{mini}</mark>" 
      stringue.append(mini)
    
  return " ".join(stringue)



if __name__ == '__main__':
    app.run(debug=True, port=8100)
    # add host='0.0.0.0' if running on docker container
