from main import cursor
from collections import defaultdict

def consultor(apendice):
    comma = \
        f""" 
        SELECT nome, tipo, qtd, data_de_chegada, codigo 
        FROM PRODUTOS_SERGEL 
        {apendice}
        ORDER BY tipo, nome
        """
    
    lista = defaultdict(list)
    for sorvete in cursor.execute(comma):
        nome, tipo, qtd, data_de_chegada, codigo = sorvete
        data_formatada = data_de_chegada.strftime('%d/%m/%Y')
        lista[tipo].append([nome, qtd, data_formatada, codigo])
    lista = dict(lista)
    return lista

def ultima_att():
    cursor.execute(
        """
        SELECT MAX(data_de_chegada) FROM PRODUTOS_SERGEL
        """)
    data_de_chegada = cursor.fetchone()[0]
    data_formatada = data_de_chegada.strftime('%d/%m/%Y')
    return data_formatada