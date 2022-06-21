from datetime import datetime
from info.basedata import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))


    def __int__(self, usuario):
        self.usuario = usuario
        