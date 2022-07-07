import json
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Starter, Main_Dish, Salad, Dessert
from flask_cors import CORS
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask (__name__)
db.init_app(app)
CORS(app)
Migrate (app, db)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASEDIR, "test.db") #Dirección provisoria de la base de datos
app.config['DEBUG'] = True

#CRUD STARTER
@app.route ('/starter', methods=['POST'])
def new_starter():
    starter= Starter()
    starter.name = request.json.get("name")
    starter.description = request.json.get("description")
    db.session.add(starter)
    db.session.commit()
    return jsonify(starter.serialize()), 200

@app.route ('/starter/<int:id>', methods=['GET'])
def get_starter(id):
    option = Starter.query.get(id)
    return jsonify(option.serialize()), 200

@app.route ('/starter/<int:id>', methods=['PUT'])
def edit_starter(id):
    edit = Starter.query.get(id)
    edit.name = request.json.get("name")
    edit.description = request.json.get("description")
    db.session.commit()
    return jsonify(edit.serialize(), '¡La entrada seleccionada ha sido actualizada!')

@app.route ('/starter/<int:id>', methods=['DELETE'])
def delete_starter(id):
    starter = Starter.query.get(id)
    db.session.delete(starter)
    db.session.commit()
    return jsonify('Entrada eliminada exitosamente')
 
#CRUD MAIN_DISH
@app.route ('/main', methods=['POST'])
def new_main():
    main= Main_Dish()
    main.name = request.json.get("name")
    main.description = request.json.get("description")
    db.session.add(main)
    db.session.commit()
    return jsonify(main.serialize()), 200

@app.route ('/main/<int:id>', methods=['GET'])
def get_main(id):
    option = Main_Dish.query.get(id)
    return jsonify(option.serialize()), 200

@app.route ('/main/<int:id>', methods=['PUT'])
def edit_main(id):
    edit = Main_Dish.query.get(id)
    edit.name = request.json.get("name")
    edit.description = request.json.get("description")
    db.session.commit()
    return jsonify(edit.serialize(), '¡El plato de fondo seleccionado ha sido actualizada!')

@app.route ('/main/<int:id>', methods=['DELETE'])
def delete_main(id):
    main = Main_Dish.query.get(id)
    db.session.delete(main)
    db.session.commit()
    return jsonify('Plato de fondo eliminado exitosamente')

#CRUD SALAD



if __name__ == '__main__':
    app.run(host='localhost', port=8000)