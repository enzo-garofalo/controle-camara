from base_de_dados import produtos

from datetime import date
data = date.today()
data = data.strftime("%x")

import oracledb
connection = oracledb.connect(user='ENZODEV', password='1234', dsn='localhost:1521/XEPDB1')
cursor = connection.cursor()

class Produto:
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo
        self._qtd = 0
        self._data = data
        self.save_to_db()

    def save_to_db(self):
        cursor.execute(
            """
            INSERT INTO PRODUTOS_SERGEL (nome, tipo, qtd, data_de_chegada)
            VALUES (:nome, :tipo, :qtd, :data_de_chegada)

            """,
            {'nome': self._nome, 'tipo': self._tipo, 'qtd': self._qtd, 'data_de_chegada': self._data}
        )
        connection.commit()

for tipo, valores in produtos.items():
    for nome in valores:
        obj = Produto(nome, tipo)