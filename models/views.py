from flask import render_template, redirect, request, session
from main import app
from .list import consultor, ultima_att

data_de_att = ultima_att()

@app.route('/')
def index():
    apendice = """ WHERE QTD > 0"""
    lista = consultor(apendice)
    return render_template('index.html', titulo='Produtos na Câmara', lista=lista, ultima_att= data_de_att)

@app.route('/redireciona')
def redireciona():
    funcao = request.args.get('funcao')
    session['funcao'] = funcao
    return render_template('redireciona.html', titulo=f'Selecione o Produto de {funcao}', ultima_att= data_de_att)

@app.route('/funcionalidade', methods=['POST', ])
def funcionalidade():
    value = request.form['valor']
    funcao = session.get('funcao')
    print(funcao)
    if funcao == 'Retirada':
        apendice = f""" WHERE QTD > 0 AND TIPO = '{value}'"""
    else:
        apendice = f""" WHERE QTD >= 0 AND TIPO = '{value}'"""
    lista = consultor(apendice)
    return render_template('funcionalidade.html', titulo=value, lista=lista, funcao=funcao, ultima_att= data_de_att)