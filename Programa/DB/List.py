from Programa.DB.base_de_dados import produtos
import oracledb

connection = oracledb.connect(user='ENZODEV', password='1234', dsn='localhost:1521/XEPDB1')
cursor = connection.cursor()

class Produto:
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo
        self._qtd = 0
        self.save_to_db()

    def save_to_db(self):
        cursor.execute(
            """
            INSERT INTO PRODUTOS_SERGEL (nome, tipo, qtd)
            VALUES (:nome, :tipo, :qtd)

            """,
            {'nome': self._nome, 'tipo': self._tipo, 'qtd': self._qtd}
        )
        connection.commit()

for tipo, valores in produtos.items():
    for nome in valores:
        obj = Produto(nome, tipo)