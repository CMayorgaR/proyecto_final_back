from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
