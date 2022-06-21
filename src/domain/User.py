from info.basedata import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(10))
   

def __init__(self, usuario) ->None:
    self.usuario = usuario
    

def __repr__(self) -> str:
    return f'User : {self.usuario}'
        