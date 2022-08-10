# -*- coding: utf-8 -*-

import numpy as np
import conexoesBD as bd
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'ofjoedjwoedmowid'

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
    return render_template('GerenciadorErro.html',
                            the_msg = "Opa! Essa página não existe :/"), 404

@app.errorhandler(400)
def erro404(error):
    return render_template('GerenciadorErro.html',
                            the_msg = "Opa! Parece que falta alguma coisa no seu código :/"), 400

@app.errorhandler(405)
def erro404(error):
    return render_template('GerenciadorErro.html',
                            the_msg = "Opa! O método utilizado para acessar essa página não é válido :/"), 405

@app.route('/')
def entry_page() -> 'html':
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def home_page() -> 'html':
    noLogin = request.form['noLogin']
    if noLogin == "Login":
        nome = (session['username'])
    elif noLogin == "noLogin":
        nome = "Sem nome de usuário"
    else:
        return redirect(url_for('entry_page'))
    return render_template('home.html',
                            the_nome = nome)

@app.route('/login', methods=['POST'])
def login() -> 'html':
    nome = str(bd.log(email = request.form['logemail'], senha = request.form['logsenha']))
    (session['username']) = nome
    return home_page()
@app.route('/missao1')
def mission1_page() -> 'html':
    return render_template('teste2.html')

if __name__ == '__main__':
    app.run(debug=True)

