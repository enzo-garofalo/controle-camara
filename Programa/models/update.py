from main import cursor, connection
from datetime import date

def update(produtos):
    data = date.today().strftime("%d-%m-%y")
    for codigo, nova_quantidade in produtos.items():
        cursor.execute(f"""SELECT qtd FROM PRODUTOS_SERGEL WHERE codigo = {codigo}""")
        quantidade_original = cursor.fetchone()[0]
        if nova_quantidade != quantidade_original:
                comma = \
                f"""
                UPDATE PRODUTOS_SERGEL
                SET qtd = {nova_quantidade}, data_de_chegada = '{data}'
                WHERE codigo = {codigo}
                """
                cursor.execute(comma)
                connection.commit() 