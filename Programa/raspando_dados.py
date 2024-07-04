import oracledb
connection = oracledb.connect(user='ENZODEV', password='1234', dsn='localhost:1521/XEPDB1')
cursor = connection.cursor()

sql_comma = """ SELECT T.DESCRICAO, S.NOME FROM SORVETES S JOIN TIPO T ON T.ID_TIPO = S.TIPO """ 
produtos = {}

for sorvete in cursor.execute(sql_comma):
  if sorvete[0] not in produtos.keys():
    produtos[sorvete[0]] = [sorvete[1]]
  else:
    produtos[sorvete[0]].append(sorvete[1])


python_file_content = f"""
produtos = {produtos}
"""

file_path = r"C:\Users\Enzo\[Workspace]\controle-camara\Programa\sorvetes_para_banco.py"
with open(file_path, 'w') as file:
  file.write(python_file_content)
