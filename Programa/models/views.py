from flask import render_template, redirect, request, session
from main import app
from .list import consultor, ultima_att

data_de_att = ultima_att()

@app.route('/')
def index():
    lista = consultor()
    return render_template('index.html', titulo='Produtos na Câmara', lista=lista, ultima_att= data_de_att)

@app.route('/redireciona')
def redireciona():
    funcao = request.args.get('funcao')
    session['funcao'] = funcao
    return render_template('redireciona.html', titulo=f'Selecione o Produto de {funcao}', ultima_att= data_de_att)

@app.route('/funcionalidade', methods=['POST', ])
def funcionalidade():
    lista = consultor()
    value = request.form['valor']
    funcao = session.get('funcao')
    produtos = lista.get(value)
    nova_lista = {}
    nova_lista[value] = produtos
    return render_template('funcionalidade.html', titulo=value, lista=nova_lista, funcao=funcao, ultima_att= data_de_att)