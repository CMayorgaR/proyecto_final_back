from codecs import backslashreplace_errors
import email
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, true

db = SQLAlchemy()

#TABLAS DE USUARIO
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    user = db.relationship('User', backref='role', lazy=True)
    

    def __repr__(self):
        return "Role %r" % self.name

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
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
        nullable=False)
    selection = db.relationship ('Selection', backref='user', lazy=True)    

    def __repr__(self):
        return "User %r>" % self.email

    def serialize(self):
        return{
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "role_id": self.role_id
        }

#TABLAS DE MENÚ
class Starter(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    date= db.Column(db.String, nullable=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    selection = db.relationship ('Selection', backref='starter', lazy=True)

    def __repr__(self):
        return "<Starter %r>" % self.starter_name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date":self.date
            }

class Main_Dish(db.Model):
    __tablename__= 'main'
    id = db.Column (db.Integer, primary_key=True)
    date= db.Column(db.String, nullable=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    selection = db.relationship ('Selection', backref='main', lazy=True)

    def __repr__(self):
        return "<Main_Dish %r>" % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date":self.date
        }

class Salad(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    date= db.Column(db.String, nullable=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    selection = db.relationship ('Selection', backref='salad', lazy=True)

    def __repr__(self):
        return "<Salad %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date":self.date
        }

class Dessert(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    date= db.Column(db.String, nullable=True)
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)
    selection = db.relationship ('Selection', backref='dessert', lazy=True)

    def __repr__(self):
        return "<Dessert %r>" % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date":self.date
        }
    
class Selection(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    date = db.Column (db.String(50), nullable=True)
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'), nullable=True)
    starter_id= db.Column (db.Integer, db.ForeignKey('starter.id'), nullable=True)
    main_id= db.Column (db.Integer, db.ForeignKey('main.id'), nullable=True)
    salad_id= db.Column (db.Integer, db.ForeignKey('salad.id'), nullable=True)
    dessert_id= db.Column (db.Integer, db.ForeignKey('dessert.id'), nullable=True)
    
    def __repr__(self):
        return "<Selection %r>" % self.name
    
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'user': self.user.email,
            'starter': self.starter.name,
            'main': self.main.name,
            'salad': self.salad.name,
            'dessert': self.dessert.name
          }