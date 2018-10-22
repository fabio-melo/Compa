from flask import Flask, render_template, request, flash
import subprocess
from factory import CompaFactory

app = Flask(__name__)
app.secret_key = 'development key'

cf = CompaFactory()

@app.route('/')
def start_server():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
  errors_spell, errors_repetition, sintagmas  = cf.execute(request.form['Text1'].lower())
  flash(errors_spell)
  """
  res = di.check_phrase(request.form['Text1'])
  if not res:
    flash("Não há erros ortográficos no texto escrito")
  else:
    for r in res:
      flash(f"A Palavra <b>{ r.replace('','  ') }</b> não está no dicionário, você quis dizer <b>{ d.correction(r).replace('','    ') }</b>?")
  """ 
  return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8100)
    # add host='0.0.0.0' if running on docker container
