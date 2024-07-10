from flask import render_template, redirect, request, session, url_for
from main import app
from .read import consultor, ultima_att
from .update import update

@app.route('/')
def index():
    data_de_att = ultima_att()
    
    apendice = """ WHERE QTD > 0 """
    lista = consultor(apendice)
    return render_template('index.html', titulo='Produtos na Câmara', lista=lista, ultima_att= data_de_att)

@app.route('/redireciona')
def redireciona():
    data_de_att = ultima_att()

    funcao = request.args.get('funcao')
    session['funcao'] = funcao
    return render_template('redireciona.html', titulo=f'Selecione o Produto de {funcao}', ultima_att= data_de_att)

@app.route('/funcionalidade', methods=['POST', ])
def funcionalidade():
    data_de_att = ultima_att()

    value = request.form['valor']
    funcao = session.get('funcao')

    if funcao == 'Retirada':
        apendice = f""" 
                    WHERE QTD > 0 AND TIPO = '{value}'
                    """
    else:
        apendice = f""" 
                    WHERE QTD >= 0 AND TIPO = '{value}'
                    """
    lista = consultor(apendice)
    return render_template('funcionalidade.html', titulo=value, lista=lista, funcao=funcao, ultima_att= data_de_att)

@app.route('/atualiza', methods=['POST', ])
def atualiza():
    codigos = request.form.getlist('cod')
    quatidades = request.form.getlist('qtd')
    quatidades_retiradas = request.form.getlist('qtd-retirada')
    
    produtos = {}
    for cod, qtd in zip(codigos, quatidades):
        produtos[cod] = qtd
    
    update(produtos)
        
    return redirect(url_for('index'))