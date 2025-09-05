from database import db
from flask_bcrypt import generate_password_hash


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    nome = db.Column(db.String(100))
    nickname = db.Column(db.String(20), unique=True)
    senha = db.Column(db.String(100))
    
    def set_senha(self, senha):
        self.senha = generate_password_hash(senha).decode('utf-8')

class Jogo(db.Model):
    __tablename__ = 'jogos'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    nome = db.Column(db.String(100), nullable = False)
    categoria = db.Column(db.String(50), nullable = False)
    console = db.Column(db.String(50), nullable = False)