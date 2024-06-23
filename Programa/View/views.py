from flask import render_template, redirect, request, session
from main import app
from .List import lista, sorvetes

@app.route('/')
def index():
    return render_template('index.html', titulo='Produtos na Câmara', sorvetes=sorvetes, lista=lista)

@app.route('/redireciona')
def redireciona():
    funcao = request.args.get('funcao')
    session['funcao'] = funcao
    return render_template('redireciona.html', titulo=f'Selecione o Produto de {funcao}')

@app.route('/funcionalidade', methods=['POST', ])
def funcionalidade():
    value = request.form['valor']
    funcao = session.get('funcao')
    produtos = lista.get(value)
    nova_lista = {}
    nova_lista[value] = produtos
    return render_template('funcionalidade.html', titulo=value, lista=nova_lista, funcao=funcao)