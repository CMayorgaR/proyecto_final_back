import email
from enum import unique
from flask_sqlalchemy import SQLAlchemy

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
    name = db.Column (db.String(100), nullable= False)
    description = db.Column (db.String(300), nullable= False)

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

    def __repr__(self):
        return "<Dessert %r>" % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    
#class Menu_Option(db.Model):
    #id = db.Column (db.Integer, primary_key=True)
