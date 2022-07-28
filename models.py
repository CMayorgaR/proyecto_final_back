from codecs import backslashreplace_errors
import email
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

#TABLAS DE USUARIO
class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return "Roles %r" % self.name

    def serialize(self):
        return{
            "id":self.id,
            "name": self.name
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    roles_id =db.Column(db.Integer)

    def __repr__(self):
        return "User %r>" % self.email

    def serialize(self):
        return{
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password,
            "roles_id": self.roles_id
        }

#TABLAS DE MENÚ
class Starter(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    #selection_id = db.Column (db.Integer, db.ForeignKey('selection.id'), nullable=False)

    def __repr__(self):
        return "<Starter %r>" % self.starter_name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
            }

class Main_Dish(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    #selection_id = db.Column (db.Integer, db.ForeignKey('selection.id'), nullable=False)

    def __repr__(self):
        return "<Main_Dish %r>" % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Salad(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    #selection_id = db.Column (db.Integer, db.ForeignKey('selection.id'), nullable=False)

    def __repr__(self):
        return "<Salad %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Dessert(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    #selection_id = db.Column (db.Integer, db.ForeignKey('selection.id'), nullable=False)

    def __repr__(self):
        return "<Dessert %r>" % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    
#class Selection(db.Model):
#    id = db.Column (db.Integer, primary_key=True)
#    date = db.Column (db.DateTime)
#    starter= db.relationship ('Starter', backref='selection', lazy=True)
#    main= db.relationship('Main_Dish', backref='selection', lazy=True)
#    salad= db.relationship('Salad', backref='selection', lazy=True)
#    dessert= db.relationship('Dessert', backref='selection', lazy=True)
    
#    def __repr__(self):
#        return "<Selection %r>" % self.name
    
#    def serialize(self):
#        return {
#            'id': self.id,
#            'date': self.date,
#            'starter': self.starter,
#            'main': self.main,
#            'salad': self.salad,
#            'dessert': self.dessert
#        }