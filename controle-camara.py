import os
import oracledb












def menu():
  os.system('cls')
  while True:
      # try:
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
              consultar()
          else:
              print("\n")
              print("--------------Até Logo!--------------")
              exit()
          # else:
          #     os.system('cls')
          #     print("------Digite valores válidos---------")
          #     continue
      # except ValueError:
      #     os.system('cls')
      #     print("------Digite valores válidos---------")
      #     continue     

if __name__ == '__main__':
  menu()