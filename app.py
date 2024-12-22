from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['ENV'] = 'development'  # Add this line to suppress the warning
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    db.create_all()
    load_initial_data()
    app.run(debug=True)