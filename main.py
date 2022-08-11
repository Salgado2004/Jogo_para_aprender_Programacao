# -*- coding: utf-8 -*-

import numpy as np
import conexoesBD as bd
import verificaMissao as vm
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'ofjoedjwoedmowid'

@app.route('/verifica', methods=['POST'])
def verifica() -> 'html':
    missao = int(request.form['missao'])
    ordem = [ ]
    codeblocks = ['var.', 'print.', 'if.', 'else.', 'elif.', 'while.', 'for.', 'list.', 'tuple.', 'set.', 'dictionary.', 'funName.', 'funCall.']
    for i in range(15):
        for code in codeblocks:
            chave = code+str(i)
            tipo = code.split(".")
            try:
                dicionario = {'index': int(request.form["indice."+str(i)]), 'valor': request.form[chave], 'tipo': tipo[0]}
                ordem.append(dicionario)
            except KeyError:
                continue
    codigo = vm.criaCodigo(ordem)
    return codigo


@app.errorhandler(404)
def erro404(error):
    return render_template('GerenciadorErro.html',
                            the_msg = "Opa! Essa página não existe :/",
                            the_erro = "404"), 404

@app.errorhandler(400)
def erro400(error):
    return render_template('GerenciadorErro.html',
                            the_msg = "Opa! Parece que falta alguma coisa no seu código :/",
                            the_erro = "400"), 400

@app.errorhandler(405)
def erro405(error):
    return render_template('GerenciadorErro.html',
                            the_msg = "Opa! O método utilizado para acessar essa página não é válido :/",
                            the_erro = "405"), 405

@app.route('/')
def entry_page() -> 'html':
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def home_page() -> 'html':
    noLogin = request.form['noLogin']
    if noLogin == "Login":
        nome = (session['username'])
        login = "1"
    elif noLogin == "noLogin":
        session.pop('username', None)
        (session['username']) = "Sem nome de usuário"
        (session['nivel']) = "1"
        nivel = (session['nivel'])
        nome = (session['username'])
        login = "0"
    else:
        return redirect(url_for('entry_page'))
    return render_template('home.html',
                            the_nome = nome,
                            the_nivel = nivel,
                            the_login = login)

@app.route('/login', methods=['POST'])
def login() -> 'html':
    session.pop('username', None)
    nome = str(bd.log(email = request.form['logemail'], senha = request.form['logsenha']))
    (session['username']) = nome
    return home_page()

@app.route('/missoes', methods=['POST'])
def get_missao() -> 'html':
    missao =  (session['nivel'])
    pagMissao = "missao"+missao+".html"
#    exec(open("codigoMissao1.py").read())
    return render_template(pagMissao, 
                            the_nivel = int(missao))

if __name__ == '__main__':
    app.run(debug=True)

