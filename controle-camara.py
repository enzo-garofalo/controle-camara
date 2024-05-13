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
            print('-'*17, 'Tipo', '-'*17)
            print("1- Pote 1 litro\n2- Pote 2 litros\n3- Picolé\n4- Bombom")
            print('-'*40)
            while True:
                tipo = int(input("Digite o tipo de Produto: "))
                if tipo > 4 or tipo < 1:
                    print()
                    print('='*8, "Digite valores válidos", '='*8)
                    continue
                else:
                    break
            nome = input("Digite o Nome: ").title()
            quantidade = 0
            break
        except ValueError:
            print('='*8, "Digite valores válidos", '='*8)
            continue
        
    print()
    print('='*40)
    cursor.execute(f"""INSERT INTO SORVETES (TIPO, NOME, QUANTIDADE) VALUES({tipo}, '{nome}', {quantidade})""")
    connection.commit()
    print("="*10, 'Produto cadastrado!', "="*9)
    print('='*40)

    escolha = input("Deseja cadastrar outro produto:\n[Sim/Não]: ").upper()
    if escolha in ['SIM', 'S']:
        cadastrar()
    else:
        decisao()

def receber():
    os.system('cls')
    tipos= {1: 'Potes 1 Litro ', 2:'Potes 2 Litros', 3:'Picolés ', 4:'Bombom'}
    for id, descricao in tipos.items():
        print(Fore.LIGHTGREEN_EX+'='*((49-len(descricao))//2), descricao, '='*((49-len(descricao))//2)+Style.RESET_ALL)
        sql_comma = f""" SELECT SORVETES.ID_PRODUTO, SORVETES.NOME, TIPO.DESCRICAO, SORVETES.QUANTIDADE 
                    FROM SORVETES 
                    JOIN TIPO ON SORVETES.TIPO = TIPO.ID_TIPO 
                    WHERE SORVETES.TIPO = {id} 
                    ORDER BY SORVETES.NOME"""
        consultor(sql_comma)
        print('='*49)
        print()


def consultor(sql_comma):
    resultado = []

    for row in cursor.execute(sql_comma):
        resultado.append(list(row))
    print(tabulate(resultado, headers=["Cod", "Nome", "Descrição", "QTDE."]))
    return 

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