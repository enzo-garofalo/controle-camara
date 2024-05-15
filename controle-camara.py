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
            while True:
                tipo = int(input("Digite a categoria do produto:"))
                if tipo > 5 or tipo < 1:
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

def receber():
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
            id = int(input("Digite qual categoria chegou: "))
            os.system('cls')
            descricao = categorias.get(id)
            if id == -1:
                menu()
            if descricao:
                print(Fore.LIGHTGREEN_EX + '='*((60-len(descricao))//2), descricao, '='*((60-len(descricao))//2) + Style.RESET_ALL)
                break
            else:
                os.system('cls')
                print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
                continue
        except ValueError:
            os.system('cls')
            print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
            continue
    
    sql_comma = f""" SELECT ID_PRODUTO, NOME, QUANTIDADE 
                FROM SORVETES 
                WHERE TIPO = {id} 
                ORDER BY NOME"""
    consultor(sql_comma)
    print(Fore.LIGHTGREEN_EX+ '='*60 +Style.RESET_ALL)
    
    while True:
        cod_nome = input(f"Digite o código ou nome do produto recém chegado: ")
        if cod_nome.isdigit():
            cod_nome = int(cod_nome)
            apendice = f"WHERE ID_PRODUTO = {cod_nome}"
        else:
            cod_nome = cod_nome.title()
            apendice = f"WHERE NOME = '{cod_nome}' AND TIPO = {id}"
        
        sql_comma = f""" SELECT ID_PRODUTO, NOME, QUANTIDADE 
                FROM SORVETES 
                {apendice} 
                ORDER BY NOME"""

        quantidade = consultor(sql_comma)

        if quantidade < 0:
            print()
            print(Fore.LIGHTRED_EX+'='*8, "Digite valores válidos", '='*8+Style.RESET_ALL)
            continue
        else: 
            nova_quantidade = int(input("Digite Quantas caixas chegou: "))
            nova_quantidade += quantidade
            cursor.execute(f""" UPDATE SORVETES SET QUANTIDADE = {nova_quantidade} {apendice} """)
            connection.commit()
        
        
        escolha = input(f"\nVocê deseja adicionar outro produto nessa categoria?\n[Sim/Não]: ").upper()
        if escolha in ['SIM', 'S']:
            continue
        elif escolha in ['N', 'NÃO', 'NAO']:
            receber()
            break

def consultor(sql_comma):
    resultado = []
    for row in cursor.execute(sql_comma):
        resultado.append(list(row))
    
    if len(resultado) < 1:
        print('Produto não existe')
        quantidade = -1
    else:
        quantidade = resultado[0][2]
        print(tabulate(resultado, headers=["Cod", "Nome", "QTDE."], tablefmt='rounded_grid'))
    
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
            receber()
        elif escolha == 3:
            cadastrar()
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