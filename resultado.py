# -*- coding: utf-8 -*-

import numpy as np 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/resultado', methods=['POST'])
def resultado() -> 'html':
    ordem = [
        {'index': int(request.form['condicionalIf.2']), 'valor': 'if('+request.form['condicaoIf.2']+'):\n'},
        {'index': int(request.form['print.10']), 'valor': '   print('+request.form['texto.10']+')\n'},
        {'index': int(request.form['print.12']), 'valor': '   print('+request.form['texto.12']+')\n'},
        {'index': int(request.form['variavel.1']), 'valor': "qtdFrutas = 10\n"},
        {'index': int(request.form['condicionalElse.11']), 'valor': "else:\n"}
    ]
    ordem.sort(key=ordena)
    arquivoCodigo = open("codigoMissao1.py", "w")
    for x in ordem:
        arquivoCodigo.write(x['valor'])
    return "o código foi baixado!"

def ordena(e):
  return e['index']

@app.errorhandler(404)
def erro404(error):
    return render_template('erro404.html'), 404

@app.errorhandler(400)
def erro404(error):
    return render_template('erro400.html'), 400

@app.route('/missao1')
def entry_page() -> 'html':
    return render_template('teste2.html')

if __name__ == '__main__':
    app.run(debug=True)

