import os
import oracledb
from tabulate import tabulate
from colorama import Fore, Style

connection = oracledb.connect(user='ENZODEV', password='1234', dsn='localhost:1521/XEPDB1')
cursor = connection.cursor()

def cadastrar():
    os.system('cls')
    while True:
        try: 
            print("="*10, 'Cadastro de Produto', "="*9)
            print('-'*14, 'Categorias', '-'*14)
            print("1- Pote 1 litro\n2- Pote 2 litros\n3- Picolé\n4- Bombom\n5- Pote de 5 Litros")
            print('-'*40)
            print(Fore.LIGHTGREEN_EX+'===== Digite -1 para voltar ao menu ===='+Style.RESET_ALL)
            while True:
                tipo = int(input("Digite a categoria do produto: "))
                if tipo == -1:
                    menu()
                    return
                elif tipo > 5 or tipo < 1:
                    os.system('cls')
                    print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
                    continue
                else:
                    break
            nome = input("Digite o Nome do novo produto: ").title()
            quantidade = 0
            break
        except ValueError:
            os.system('cls')
            print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
            continue
        
    print()
    print('='*40)
    cursor.execute(f"""INSERT INTO SORVETES (TIPO, NOME, QUANTIDADE) VALUES({tipo}, '{nome}', {quantidade})""")
    connection.commit()
    print("="*10, 'Produto cadastrado!', "="*9)
    print('='*40)

    while True:
        escolha = input(f"Você deseja cadastrar outro produto?\n[Sim/Não]: ").upper()
        if escolha in ['SIM', 'S']:
            cadastrar()
        elif escolha in ['N', 'NÃO', 'NAO']:
            decisao()
        else:
            print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
            continue

def selecionar_categoria_entrada():
    os.system('cls')
    categorias= {1: 'Potes 1 Litro', 
                 2:'Potes 2 Litros', 
                 3:'Picolés', 
                 4:'Bombom', 
                 5:'Potes 5 litros'}
    while True:
        try:
            print('-'*14, 'Categorias', '-'*14)
            print("1- Pote 1 litro\n2- Pote 2 litros\n3- Picolé\n4- Bombom\n5- Pote de 5 Litros")
            print('-'*40)
            print(Fore.LIGHTGREEN_EX+'===== Digite -1 para voltar ao menu ===='+Style.RESET_ALL)
            categoria = int(input("Digite qual categoria chegou: "))
            os.system('cls')
            descricao = categorias.get(categoria)
            if categoria == -1:
                menu()
            elif descricao:
                break
            else:
                os.system('cls')
                print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
                continue
        except ValueError:
            os.system('cls')
            print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
            continue
    
    return categoria

def entrada():
    categoria = selecionar_categoria_entrada()

    sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO,S.QUANTIDADE 
                     FROM SORVETES S 
                     JOIN TIPO T ON S.TIPO = T.ID_TIPO
                     WHERE S.TIPO = {categoria}
                     ORDER BY S.NOME """
    consultor(sql_comma)
    
    while True:
        cod_nome = input(f"Digite o código ou nome do produto recém chegado: ")
        if cod_nome.isdigit():
            cod_nome = int(cod_nome)
            apendice = f"WHERE ID_PRODUTO = {cod_nome}"
        else:
            cod_nome = cod_nome.title()
            apendice = f"WHERE NOME = '{cod_nome}' AND TIPO = {id}"
        
        os.system('cls')
        sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO, S.QUANTIDADE 
                     FROM SORVETES S 
                     JOIN TIPO T ON S.TIPO = T.ID_TIPO
                     {apendice}
                     ORDER BY S.NOME """
        quantidade = consultor(sql_comma)

        if quantidade < 0:
            print(Fore.LIGHTRED_EX+'='*8, "Produto Não existe", '='*8+Style.RESET_ALL)
            print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
            continue
        else: 
            print(Fore.LIGHTGREEN_EX+'===== Digite -1 se esse o produto estiver incorreto ===='+Style.RESET_ALL)
            nova_quantidade = int(input("Digite Quantas caixas chegou: "))
            if nova_quantidade == -1:
                entrada()
                break
            else:
                nova_quantidade += quantidade
                cursor.execute(f""" UPDATE SORVETES SET QUANTIDADE = {nova_quantidade} {apendice} """)
                consultor(sql_comma)
                connection.commit()
                break
             
    escolha = input(f"\nVocê Deseja Adicionar Outro Produto a Câmara?\n[Sim/Não]: ").upper()
    if escolha in ['SIM', 'S']:
        entrada()
    else:
        menu()

def saida():
    os.system('cls')
    categorias= { 1: 'Potes 1 Litro', 2:'Potes 2 Litros', 3:'Picolés', 4:'Bombom', 5:'Potes 5 litros' }
    # PRODUTOS QUE HÁ NA CÂMARA
    for categoria in categorias.keys():
        sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO,S.QUANTIDADE 
                         FROM SORVETES S 
                         JOIN TIPO T ON S.TIPO = T.ID_TIPO
                         WHERE S.TIPO = {categoria} AND S.QUANTIDADE > 0
                         ORDER BY S.NOME"""
        consultor(sql_comma)
    
    while True:
        cod_nome = input(f"Digite o código ou nome do produto para pedido: ")
        if cod_nome.isdigit():
            cod_nome = int(cod_nome)
            apendice = f"WHERE ID_PRODUTO = {cod_nome}"
        else:
            cod_nome = cod_nome.title()
            apendice = f"WHERE NOME = '{cod_nome}' AND TIPO = {id}"
        
        os.system('cls')
        sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO, S.QUANTIDADE 
                     FROM SORVETES S 
                     JOIN TIPO T ON S.TIPO = T.ID_TIPO
                     {apendice}
                     ORDER BY S.NOME """

        quantidade = consultor(sql_comma)
        if quantidade < 0:
            print(Fore.LIGHTRED_EX+'='*8, "Produto Não existe", '='*8+Style.RESET_ALL)
            print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
            continue
        elif quantidade == 0:
            print(Fore.LIGHTRED_EX+'='*8, "Não há caixas na Câmara", '='*8+Style.RESET_ALL)
            continue
        else: 
            print(Fore.LIGHTGREEN_EX+'===== Digite -1 se esse o produto estiver incorreto ===='+Style.RESET_ALL)
            nova_quantidade = int(input("Digite Quantas Caixas retirar: "))
            if nova_quantidade == -1:
                entrada()
                break
            else:
                nova_quantidade += quantidade
                cursor.execute(f""" UPDATE SORVETES SET QUANTIDADE = {nova_quantidade} {apendice} """)
                consultor(sql_comma)
                connection.commit()
                break


def consultor(sql_comma):
    resultado = []
    for row in cursor.execute(sql_comma):
        resultado.append(list(row))
    
    if len(resultado) < 1:
        quantidade = -1
    else:
        quantidade = resultado[0][3]
        print(Fore.LIGHTGREEN_EX + '='*80 + Style.RESET_ALL)
        print(tabulate(resultado, headers=["Cod", "Nome", "Categoria", "QTDE."], tablefmt='rounded_grid'))
        print(Fore.LIGHTGREEN_EX+ '='*80 +Style.RESET_ALL)
    
    return quantidade

def decisao():
    while True:
        escolha = input(f"\nVocê deseja retornar ao menu?\n[Sim/Não]: ")
        escolha = escolha.upper()
        if escolha in ["SIM", "S"]:
            os.system("cls")
            menu()
        elif escolha in ["NÃO", "NAO", "N"]:
            print('='*15, 'Até Logo!', '='*14)
            exit()
        else:
            print('='*4+" Digite uma opção válida! "+'='*4)
            continue
        
def menu():
  os.system('cls')
  while True:
    try:
        print("="*10, 'Controle de Câmara', "="*10)
        print("----------| 1- Cadastrar    |-----------")
        print("----------| 2- Receber      |-----------")
        print("----------| 3- Retirar      |-----------")
        print("----------| 4- Sair         |-----------")
        print("="*40)
        escolha = int(input("O que deseja fazer: "))
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            entrada()
        elif escolha == 3:
            saida()
        elif escolha == 4:
           print('='*15, 'Até Logo!', '='*14)
           exit()
        else:
            os.system('cls')
            print('='*8, "Digite valores válidos", '='*8)
            continue
        break
    except ValueError:
        os.system('cls')
        print('='*8, "Digite valores válidos", '='*8)
        continue     

if __name__ == '__main__':
  menu()