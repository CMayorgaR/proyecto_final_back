from crypt import methods
import email
import json
import os
import re
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from models import db, Starter, Main_Dish, Salad, Dessert, User, Role #, Selection
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


BASEDIR = os.path.abspath(os.path.dirname(__file__))
app = Flask (__name__)
db.init_app(app)
CORS(app)
Migrate (app, db)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASEDIR, "test.db") #Dirección provisoria de la base de datos
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secreta'
app.config['JWT_SECRET_KEY'] = 'mas-secreta-aun'

#CRUD USER
@app.route ('/', methods=["GET"])
def home():
    return 'Hello flask apiiiiii'

email_reg = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
password_reg = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

@app.route ('/create_user', methods=["POST"])
def create_user():
    email = request.json.get("email")
    password = request.json.get("password")
    if email != '' and re.search(email_reg, email):
        user = User.query.filter_by(email=email).first()
        if user is not None:
            return jsonify({
                "msg":'User already exist'
            }),400
        else:
            if password != '' and re.search(password_reg, password):
                user = User()
                user.email = email
                password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')
                user.password = password_hash
                user.full_name = request.json.get("full_name")
                user.role_id = 1

                db.session.add(user)
                db.session.commit()

                return jsonify({
                    "msg": "success user created"
                }), 200
            else:
                return jsonify({
                    "msg": 'Wrong password format'
                }), 400
    else:
        return jsonify({
                    "msg": 'Wrong email format'
                }), 400

@app.route('/login', methods=["POST"])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if password == '' and email == '':
        return jsonify({
            "msg": 'Email or password empty'
        }), 400
    else:
        user = User.query.filter_by(email=email).first()
        if user is not None:
            check_password = bcrypt.check_password_hash(user.password, password)
            if check_password:
                access_token = create_access_token(identity=email)
                
                if user.role_id == 1:
                    return jsonify({
                        "user": user.serialize(),
                        "access_token":access_token,
                        
                    }), 200
                else:
                    return jsonify({
                        "user": user.serialize(),
                        "access_token":access_token,
                        "role_id": 2
                        
                    }), 200
            else:
                return jsonify({
                    "msg": 'email or password is invalid'
                }), 400
        else:
            return jsonify({
                "msg": 'user not found, go to register'
            }), 400

@app.route('/me', methods=["GET"])
@jwt_required()
def me():
    user = get_jwt_identity()
    return jsonify(user), 200

#CRUD STARTER
@app.route ('/starter', methods=['POST'])
def new_starter():
    if request.json.get("name") != "" and request.json.get("description") != "":
        starter= Starter()
        starter.name = request.json.get("name")
        starter.description = request.json.get("description")
        starter.date = request.json.get("date")
        db.session.add(starter)
        db.session.commit()
        return jsonify(starter.serialize()), 200
    else:
        return jsonify("Este campo no puede estar vacío")
    
@app.route ('/starter/<int:id>', methods=['GET']) #One Starter
def get_starter(id):
    option = Starter.query.get(id)
    return jsonify(option.serialize()), 200

@app.route ('/starter', methods = ['GET']) #All starters
def all_starters():
    starters= Starter.query.all()
    starters= list(map(lambda x: x.serialize(), starters))
    return jsonify(starters), 200

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
    if request.json.get("name") != "" and request.json.get("description") != "":
        main= Main_Dish()
        main.name = request.json.get("name")
        main.description = request.json.get("description")
        main.date = request.json.get("date")
        db.session.add(main)
        db.session.commit()
        return jsonify(main.serialize()), 200
    else:
        return jsonify("Este campo no puede estar vacío")

@app.route ('/main/<int:id>', methods=['GET']) #One Main_Dish
def get_main(id):
    option = Main_Dish.query.get(id)
    return jsonify(option.serialize()), 200

@app.route ('/main', methods = ['GET']) #All Main_Dishes
def all_main():
    mains = Main_Dish.query.all()
    mains= list(map(lambda x: x.serialize(), mains))
    return jsonify(mains), 200

@app.route ('/main/<int:id>', methods=['PUT'])
def edit_main(id):
    edit = Main_Dish.query.get(id)
    edit.name = request.json.get("name")
    edit.description = request.json.get("description")
    db.session.commit()
    return jsonify(edit.serialize(), '¡El plato de fondo seleccionado ha sido actualizado!')

@app.route ('/main/<int:id>', methods=['DELETE'])
def delete_main(id):
    main = Main_Dish.query.get(id)
    db.session.delete(main)
    db.session.commit()
    return jsonify('Plato de fondo eliminado exitosamente')

#CRUD SALAD
@app.route ('/salad', methods=['POST'])
def new_salad():
    if request.json.get("name") != "" and request.json.get("description") != "":
        salad= Salad()
        salad.name = request.json.get("name")
        salad.description = request.json.get("description")
        salad.date = request.json.get("date")
        db.session.add(salad)
        db.session.commit()
        return jsonify(salad.serialize()), 200
    else:
        return jsonify("Este campo no puede estar vacío")    

@app.route ('/salad/<int:id>', methods=['GET']) #One Salad
def get_salad (id):
    option = Salad.query.get(id)
    return jsonify(option.serialize()), 200

@app.route ('/salad', methods = ['GET']) #All salads
def all_salads():
    salads = Salad.query.all()
    salads = list(map(lambda x: x.serialize(), salads))
    return jsonify(salads), 200

@app.route ('/salad/<int:id>', methods=['PUT'])
def edit_salad(id):
    edit = Salad.query.get(id)
    edit.name = request.json.get("name")
    edit.description = request.json.get("description")
    db.session.commit()
    return jsonify(edit.serialize(), '¡La ensalada seleccionada ha sido actualizada!')

@app.route ('/salad/<int:id>', methods=['DELETE'])
def delete_salad(id):
    salad= Salad.query.get(id)
    db.session.delete(salad)
    db.session.commit()
    return jsonify('La ensalada fue eliminada exitosamente')

#CRUD DESSERT
@app.route ('/dessert', methods=['POST'])
def new_dessert():
    if request.json.get("name") != "" and request.json.get("description") != "":
        dessert= Dessert()
        dessert.name = request.json.get("name")
        dessert.description = request.json.get("description")
        dessert.date = request.json.get("date")
        db.session.add(dessert)
        db.session.commit()
        return jsonify(dessert.serialize()), 200
    else:
        return jsonify("Este campo no puede estar vacío")

@app.route ('/dessert/<int:id>', methods=['GET']) #One dessert
def get_dessert (id):
    option = Dessert.query.get(id)
    return jsonify(option.serialize()), 200

@app.route ('/dessert', methods = ['GET']) #All desserts
def all_desserts():
    desserts = Dessert.query.all()
    desserts = list(map(lambda x: x.serialize(), desserts))
    return jsonify(desserts), 200

@app.route ('/dessert/<int:id>', methods=['PUT'])
def edit_dessert(id):
    edit = Dessert.query.get(id)
    edit.name = request.json.get("name")
    edit.description = request.json.get("description")
    db.session.commit()
    return jsonify(edit.serialize(), '¡El postre seleccionado ha sido actualizado!')

@app.route ('/dessert/<int:id>', methods=['DELETE'])
def delete_dessert(id):
    dessert= Dessert.query.get(id)
    db.session.delete(dessert)
    db.session.commit()
    return jsonify('El postre fue eliminado exitosamente')


#CRUD SELECTION
#@app.route ('/userselection', methods=['POST'])
#def add_user_selection():
#    selected_starter= Starter.query\
#        .join(Starter, Starter.id == Selection.starter_id)\
#        .add_columns(Starter.id, Starter.name, Starter.description)\
#        .request.json.get(Starter.name, Starter.description)
#    db.session.add(selected_starter)
#    db.session.commit()
#    return jsonify(selected_starter.serialize(), 200)    


if __name__ == '__main__':
    app.run(host='localhost', port=8080)