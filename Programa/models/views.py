from flask import render_template, redirect, request, session
from main import app, cursor, connection
from collections import defaultdict

lista = defaultdict(list)

for sorvete in cursor.execute(""" SELECT nome, tipo, qtd, data_de_chegada FROM PRODUTOS_SERGEL WHERE QTD > 0  """):
    nome, tipo, qtd, data_de_chegada = sorvete
    data_formatada = data_de_chegada.strftime('%d/%m/%Y')
    lista[tipo].append([nome, qtd, data_formatada])
lista = dict(lista)

@app.route('/')
def index():
    return render_template('index.html', titulo='Produtos na Câmara', lista=lista)

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