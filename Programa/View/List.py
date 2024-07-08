from sorvetes_para_banco import produtos

class Produto:
    produtos = []
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo
        self._qtd = 0

        Produto.produtos.append(self)
    def __str__(self):
        return f'Nome: {self._nome}\n'\
               f'     Tipo: {self._tipo}\n'\
               f'     Qtd:  {self._qtd}\n'\
               '-----------------------------'
    @classmethod
    def consultar_produto(cls):
        for produto in cls.produtos:
            print(produto)

cont = 0
for tipo, valores in produtos.items():
    for nome in valores:
        cont += 1
        obj = Produto(nome, tipo)

Produto.consultar_produto()
print(cont)

lista= Produto.produtos

