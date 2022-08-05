# -*- coding: utf-8 -*-

import numpy as np 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/resultado', methods=['POST'])
def resultado() -> 'html':
    ordem = [
        {'index': int(request.form['condicionalIf2']), 'valor': 'if('+request.form['condicaoIf2']+'):\n'},
        {'index': int(request.form['print10']), 'valor': '   print('+request.form['texto10']+')\n'},
        {'index': int(request.form['print1012']), 'valor': '   print('+request.form['texto1012']+')\n'},
        {'index': int(request.form['variavel1']), 'valor': "qtdFrutas = 10\n"},
        {'index': int(request.form['condicionalElse11']), 'valor': "else:\n"}
    ]
    ordem.sort(key=ordena)
    arquivoCodigo = open("codigoMissao1.py", "w")
    for x in ordem:
        arquivoCodigo.write(x['valor'])
    return "o código foi baixado!"

def ordena(e):
  return e['index']

@app.route('/teste2')
def entry_page() -> 'html':
    return render_template('teste2.html')

if __name__ == '__main__':
    app.run(debug=True)

