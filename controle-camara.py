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
    tipos= {1: 'Potes 1 Litro', 2:'Potes 2 Litros', 3:'Picolés', 4:'Bombom', 5:'Potes 5 litros'}
    for id, descricao in tipos.items():
        print(Fore.LIGHTBLUE_EX+'='*((60-len(descricao))//2), descricao, '='*((60-len(descricao))//2)+Style.RESET_ALL)
        sql_comma = f""" SELECT SORVETES.ID_PRODUTO, SORVETES.NOME, SORVETES.QUANTIDADE 
                    FROM SORVETES 
                    WHERE SORVETES.TIPO = {id} 
                    ORDER BY SORVETES.NOME"""
        consultor(sql_comma)
        print('='*60)
        print()


def consultor(sql_comma):
    resultado = []
    for row in cursor.execute(sql_comma):
        resultado.append(list(row))
    print(tabulate(resultado, headers=["Cod", "Nome", "QTDE."], tablefmt='rounded_grid'))
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