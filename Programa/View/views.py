from flask import render_template
from main import app


@app.route('/')
def index():
    sorvetes= {'1 litro':['Leitinho Trufado', 3, '12/05/24'], 
               '2 litros':['Leitinho Trufado', 4, '12/12/23'],
               '5 litros':['Chocolate c/ Pedaços', 5, '10/12/23']}

    return render_template('index.html', titulo='Controle De Estoque', sorvetes = sorvetes)