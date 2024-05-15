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
            print(Fore.YELLOW+"="*29, 'Cadastro de Produto', "="*30+Style.RESET_ALL)
            submenu()
            while True:
                tipo = int(input("Digite a categoria do produto: "))
                if tipo == -1:
                    menu()
                    return
                elif tipo > 5 or tipo < 1:
                    print()
                    print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
                    continue
                else:
                    break
            nome = input("Digite o Nome do novo produto: ").title()
            quantidade = 0
            break
        except ValueError:
            print()
            print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
            continue
        
    print()
    print(Fore.YELLOW+'='*80+Style.RESET_ALL)
    cursor.execute(f"""INSERT INTO SORVETES (TIPO, NOME, QUANTIDADE) VALUES({tipo}, '{nome}', {quantidade})""")
    connection.commit()
    print("="*29, 'Produto cadastrado!', "="*30)
    print(Fore.YELLOW+'='*80+Style.RESET_ALL)

    while True:
        escolha = input(f"Você deseja cadastrar outro produto?\n[Sim/Não]: ").upper()
        if escolha in ['SIM', 'S']:
            cadastrar()
        elif escolha in ['N', 'NÃO', 'NAO']:
            decisao()
        else:
            print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)       
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
            print(Fore.YELLOW+"="*30, 'Entrada de Produto', "="*30+Style.RESET_ALL)
            submenu()
            categoria = int(input("Digite qual categoria chegou: "))
            os.system('cls')
            descricao = categorias.get(categoria)
            if categoria == -1:
                menu()
            elif descricao:
                break
            else:
                print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
                continue
        except ValueError:
            os.system('cls')
            print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
            continue
    
    return categoria

def entrada():
    categoria = selecionar_categoria_entrada()

    while True:
        sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO,S.QUANTIDADE 
                        FROM SORVETES S 
                        JOIN TIPO T ON S.TIPO = T.ID_TIPO
                        WHERE S.TIPO = {categoria}
                        ORDER BY S.NOME """
        consultor(sql_comma)
        cod_nome = input(f"Digite o código ou nome do produto recém chegado: ")
        if cod_nome.isdigit():
            cod_nome = int(cod_nome)
            apendice = f"WHERE ID_PRODUTO = {cod_nome}"
        else:
            cod_nome = cod_nome.title()
            apendice = f"WHERE NOME = '{cod_nome}' AND TIPO = {categoria}"
        
        os.system('cls')
        sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO, S.QUANTIDADE 
                     FROM SORVETES S 
                     JOIN TIPO T ON S.TIPO = T.ID_TIPO
                     {apendice}
                     ORDER BY S.NOME """
        quantidade = consultor(sql_comma)

        if quantidade < 0:
            consultor(sql_comma)
            print(Fore.LIGHTRED_EX+'='*30, "Produto Não existe", '='*30+Style.RESET_ALL)
            print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
            continue
        else: 
            print('='*16,'Digite -1 se esse o produto estiver incorreto','='*17)
            print(Fore.YELLOW+'='*80+Style.RESET_ALL)
            while True:
                try:
                    nova_quantidade = int(input("Digite Quantas caixas chegou: "))
                    break
                except ValueError:
                    print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
                    continue
            if nova_quantidade == -1:
                entrada()
                break
            else:
                nova_quantidade += quantidade
                att_camara(nova_quantidade, apendice, sql_comma)
                break
             
    escolha = input(f"\nVocê Deseja Adicionar Outro Produto a Câmara?\n[Sim/Não]: ").upper()
    if escolha in ['SIM', 'S']:
        entrada()
    else:
        menu()

def saida():
    os.system('cls')
    print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
    print ('='*30, 'Produtos Na Câmara', '='*30)
    print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
    consultor_total()
    while True:
        try:
            cod_nome = int(input(f"Digite o código do produto para retirar da câmara: "))
            apendice = f"WHERE ID_PRODUTO = {cod_nome}"
        except ValueError:
            os.system('cls')
            print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
            print ('='*30, 'Produtos Na Câmara', '='*30)
            print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
            consultor_total()
            print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
            continue

        os.system('cls')
        sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO, S.QUANTIDADE 
                     FROM SORVETES S 
                     JOIN TIPO T ON S.TIPO = T.ID_TIPO
                     {apendice}
                     ORDER BY S.NOME """

        quantidade = consultor(sql_comma)
        if quantidade < 0:
            print(Fore.LIGHTRED_EX+'='*30, "Produto Não existe", '='*30+Style.RESET_ALL)
            print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
            continue
        elif quantidade == 0:
            os.system('cls')
            print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
            print ('='*30, 'Produtos Na Câmara', '='*30)
            print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
            consultor_total()
            print('='*20, "Não há caixas desse produto na câmara", '='*21)
            print('='*29, "Digite outro código", '='*30)
            print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
            continue
        else:
            while True:                
                print('='*16,'Digite -1 se esse o produto estiver incorreto','='*17)
                print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
                try:
                    quantidade_retirada = int(input("Digite Quantas Caixas retirar: "))
                    if quantidade_retirada == -1:
                        entrada()
                        break
                    elif quantidade_retirada > quantidade:
                        os.system('cls')
                        consultor(sql_comma)
                        print(Fore.LIGHTRED_EX+'='*24, f"Há apenas {quantidade} caixas na câmara", '='*25+Style.RESET_ALL)
                        continue
                    else:
                        break
                except ValueError:
                    os.system('cls')
                    consultor(sql_comma)
                    print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
                    continue
           
        quantidade -= quantidade_retirada
        att_camara(quantidade, apendice, sql_comma)
        cursor.execute(f""" INSERT INTO PEDIDO (ID_PRODUTO, QUANTIDADE) 
                            VALUES ({cod_nome}, {quantidade_retirada}) """)
        connection.commit()
        
        escolha = input("\nVocê deseja acrescentar outro produto ao pedido?\n[Sim/Não]: ").upper()
        if escolha in ['SIM', 'S']:
            saida()
        else:
            os.system('cls')
            print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
            print('='*29,'Pedido para retirada', '='*29)
            print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
            sql_comma = """ SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO, P.QUANTIDADE
                             FROM PEDIDO P
                             JOIN SORVETES S ON P.ID_PRODUTO = S.ID_PRODUTO
                             JOIN TIPO T ON S.TIPO = T.ID_TIPO """
            consultor(sql_comma)
            cursor.execute(""" DELETE FROM PEDIDO """)
            connection.commit()
        
        decisao()

def consultor_total():
    categorias= { 1: 'Potes 1 Litro', 2:'Potes 2 Litros', 3:'Picolés', 4:'Bombom', 5:'Potes 5 litros' }
    for categoria in categorias.keys():
        sql_comma = f""" SELECT S.ID_PRODUTO, S.NOME, T.DESCRICAO,S.QUANTIDADE 
                         FROM SORVETES S 
                         JOIN TIPO T ON S.TIPO = T.ID_TIPO
                         WHERE S.TIPO = {categoria} AND S.QUANTIDADE > 0
                         ORDER BY S.NOME"""
        consultor(sql_comma)
    return

def consultor(sql_comma):
    resultado = []
    for row in cursor.execute(sql_comma):
        resultado.append(list(row))
    
    if len(resultado) < 1:
        quantidade = -1
    else:
        quantidade = resultado[0][3]
        print(tabulate(resultado, headers=["Cod", "Nome", "Categoria", "QTDE."], tablefmt='rounded_grid'))
        print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
    
    return quantidade

def att_camara(qtde, apendice, sql_comma):
    cursor.execute(f""" UPDATE SORVETES SET QUANTIDADE = {qtde} {apendice} """)
    print()
    print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
    print('='*31, 'Câmara Atualizada', '='*30)
    print(Fore.YELLOW+ '='*80 +Style.RESET_ALL)
    consultor(sql_comma)
    connection.commit()
    return

def decisao():
    while True:
        escolha = input(f"\nVocê deseja retornar ao menu?\n[Sim/Não]: ")
        escolha = escolha.upper()
        if escolha in ["SIM", "S"]:
            os.system("cls")
            menu()
        elif escolha in ["NÃO", "NAO", "N"]:
            print(Fore.YELLOW+'\n'+'='*80+Style.RESET_ALL)
            print('='*34, 'Até Logo!', '='*35)
            print (Fore.YELLOW+'='*80+Style.RESET_ALL)
            exit()
        else:
            print(Fore.LIGHTRED_EX+'='*28, "Digite valores válidos", '='*28+Style.RESET_ALL)
            continue

def submenu():
    print('-'*34,'Categorias', '-'*34)
    print("1- Pote 1 litro\n2- Pote 2 litros\n3- Picolé\n4- Bombom\n5- Pote de 5 Litros")
    print('-'*80)
    print(Fore.YELLOW+'='*80+Style.RESET_ALL)
    print('='*25,'Digite -1 para voltar ao menu','='*24)
    print(Fore.YELLOW+'='*80+Style.RESET_ALL)
    return

def menu():
  os.system('cls')
  while True:
    try:
        print(Fore.YELLOW+'='*60+Style.RESET_ALL)
        print("="*20, 'Controle de Câmara', "="*20)
        print(Fore.YELLOW+'='*60+Style.RESET_ALL)
        print('-'*20+"| 1- Cadastrar    |"+'-'*21)
        print('-'*20+"| 2- Entrada      |"+"-"*21)
        print('-'*20+"| 3- Saída        |"+"-"*21)
        print('-'*20+"| 4- Sair         |"+"-"*21)
        print(Fore.YELLOW+'='*60+Style.RESET_ALL)
        escolha = int(input("O que deseja fazer: "))
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            entrada()
        elif escolha == 3:
            saida()
        elif escolha == 4:
            print(Fore.YELLOW+'\n'+'='*60+Style.RESET_ALL)
            print('='*24, 'Até Logo!', '='*25)
            print (Fore.YELLOW+'='*60+Style.RESET_ALL)
            exit()
        else:
            os.system('cls')
            print(Fore.LIGHTRED_EX+'='*18, "Digite valores válidos", '='*18+Style.RESET_ALL)
            continue
        break
    except ValueError:
        os.system('cls')
        print(Fore.LIGHTRED_EX+'='*18, "Digite valores válidos", '='*18+Style.RESET_ALL)
        continue     

if __name__ == '__main__':
  menu()