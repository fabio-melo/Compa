"""gerar uma lista de verbos regulares"""
vari_ar, vari_er, vari_ir = [], [], []
with open('misc/geradores/verbosregulares.txt','r',encoding='utf-8') as verbos:
  for x in verbos.readlines():
    if x.rstrip()[-2:] == 'ar':
      vari_ar.append(x.rstrip()[:-2])
    elif x.rstrip()[-2:] == 'er':
      vari_er.append(x.rstrip()[:-2])
    else:
      vari_ir.append(x.rstrip()[:-2])

final = []


def build_list(vari):
  for x in vari:
    for y in primeira_pessoa_singular:
      new = [x + y]
      new.append('INDF')
      new.append('singular')
      new.append('primeira')
      final.append(new)
      for y in segunda_pessoa_singular:
        new = [x + y]
        new.append('INDF')
        new.append('singular')
        new.append('segunda')
        final.append(new)

    for y in terceira_pessoa_singular:
      new = [x + y]
      new.append('INDF')
      new.append('singular')
      new.append('terceira')
      final.append(new)

    for y in primeira_pessoa_plural:
      new = [x + y]
      new.append('INDF')
      new.append('plural')
      new.append('primeira')
      final.append(new)
      for y in segunda_pessoa_plural:
        new = [x + y]
        new.append('INDF')
        new.append('plural')
        new.append('segunda')
        final.append(new)

    for y in terceira_pessoa_plural:
      new = [x + y]
      new.append('INDF')
      new.append('plural')
      new.append('terceira')
      final.append(new)



# TERMINANDO EM AR
primeira_pessoa_singular = ['o', 'ava', 'ei','ara','arei','aria',]
segunda_pessoa_singular = ['as','avas','aste','aras','arás','arias']
terceira_pessoa_singular = ['a','ava','ou','ara','ará','aria',]
primeira_pessoa_plural = ['amos','ávamos','amos','áramos','aremos', 'aríamos',]
segunda_pessoa_plural = ['ais','áveis','astes','áreis','areis','aríeis',]
terceira_pessoa_plural = ['am','avam','aram','arão','ariam',]

build_list(vari_ar)

#TERMINANDO EM ER

primeira_pessoa_singular = ['o', 'ia','i','era','erei','eria']
segunda_pessoa_singular = ['es', 'ias','este','eras','erás','erias']
terceira_pessoa_singular = ['e','ia','eu','era','erá','eria']
primeira_pessoa_plural = ['emos','íamos','êramos','eremos','eríamos']
segunda_pessoa_plural = ['eis','íeis','estes','êreis','ereis','íeis']
terceira_pessoa_plural = ['em','iam','eram','erão','eriam']

build_list(vari_er)

#TERMINADO EM IR

primeira_pessoa_singular = ['o', 'ava', 'ei','ara','arei','aria',]
segunda_pessoa_singular = ['as', 'avas', 'aste','aras','arás','arias',]
terceira_pessoa_singular = ['e','ia','iu','ira','irá','iria']
primeira_pessoa_plural = ['imos','íamos','imos','íramos','iremos','iríamos']
segunda_pessoa_plural = ['is','íeis','istes','íreis','ireis','iríeis']
terceira_pessoa_plural = ['em','iam','iram','irão','iriam',]

build_list(vari_ir)

# removendo entradas repetidas
print(len(final))

dedup = []
for elem in final:
    if elem not in dedup:
        dedup.append(elem)

print(len(dedup))
final = dedup



import csv

with open("verbosregulares.csv", "w", newline='',encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerows(final)