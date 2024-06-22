from flask import render_template, redirect, request, session
from main import app
from collections import defaultdict

class Produto():
    def __init__(self, nome, quantidade, tipo, data):
        self.nome = nome
        self.quantidade = quantidade
        self.tipo = tipo
        self.data = data

produto1 = Produto('Leitinho Trufado', 2, 'Pote 1 Litro', '10/10/24')
produto2 = Produto('Chocolate c/ avelã', 0, 'Pote 1 Litro', '10/10/24')
produto7 = Produto('Leitinho c/ Frutas Vermelhas', 4, 'Pote 1 Litro', '10/10/24')
produto7 = Produto('Mousseee', 4, 'Pote 1 Litro', '10/10/24')
produto3 = Produto('Leitinho Trufado', 6, 'Pote 2 Litros', '10/10/24')
produto4 = Produto('Morango C/ Chocolate', 2, 'Pote 2 Litros', '10/10/24')
produto5 = Produto('Creme', 2, 'Pote 5 Litro', '10/10/24')
produto6 = Produto('Três Chocolates', 2, 'Pote 5 Litro', '10/10/24')
sorvetes = [produto1, produto2, produto3, produto4, produto5, produto6, produto7]

lista = defaultdict(list)
for sorvete in sorvetes:
    lista[sorvete.tipo].append([sorvete.nome, sorvete.quantidade, sorvete.data])

lista = dict(lista)
@app.route('/')
def index():

    return render_template('index.html', titulo='Produtos na Câmara', sorvetes = sorvetes, lista=lista)

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
    return render_template('funcionalidade.html', titulo=value+funcao, lista=nova_lista, funcao=funcao)