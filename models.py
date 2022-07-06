from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#TABLAS DE MENÚ
class Starter(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    starter_name = db.Column (db.String(100), nullable= False)
    starter_des = db.Column (db.String(300), nullable= False)

    def __repr__(self):
        return "<Starter %r>" % self.starter_name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.starter_name,
            "description": self.starter_des
            }

class Main_Dish(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    main_name = db.Column (db.String(100), nullable= False)
    main_des = db.Column (db.String(300), nullable= False)

    def __repr__(self):
        return "<Main_Dish %r>" % self.main_name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.main_name,
            "description": self.main_des
        }

class Salad(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    salad_name = db.Column (db.String(100), nullable= False)
    salad_des = db.Column (db.String(300), nullable= False)

    def __repr__(self):
        return "<Salad %r>" % self.salad_name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.salad_name,
            "description": self.salad_des
        }

class Dessert(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    dessert_name = db.Column (db.String(100), nullable= False)
    dessert_des = db.Column (db.String(300), nullable= False)

    def __repr__(self):
        return "<Dessert %r>" % self.dessert_name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.salad_name,
            "description": self.salad_des
        }
    
#class Menu_Option(db.Model):
    #id = db.Column (db.Integer, primary_key=True)
