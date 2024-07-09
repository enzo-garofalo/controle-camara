from flask import Flask
import oracledb


app = Flask(__name__)
app.secret_key = '1234'


connection = oracledb.connect(user='ENZODEV', password='1234', dsn='localhost:1521/XEPDB1')
cursor = connection.cursor()

from models.views import * 

if __name__ == '__main__':
    app.run(debug=True)

