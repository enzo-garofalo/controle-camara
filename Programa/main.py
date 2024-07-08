from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '1234'

# db = SQLAlchemy(app)

from View.views import * 

if __name__ == '__main__':
    app.run(debug=True)

