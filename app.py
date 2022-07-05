import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_cors import CORS
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask (__name__)
db.init_app(app)
CORS(app)
#Migrate (app, db)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASEDIR, "test.db") #Dirección provisoria de la base de datos
app.config['DEBUG'] = True







if __name__ == '__main__':
    app.run(host='localhost', port=8000)