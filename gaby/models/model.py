from database import db

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cargo = db.Column(db.String(120), nullable=False)
    senha = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(20), unique=True,nullable=False)
    salario = db.Column(db.Float, nullable=False)  

class Prato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True,nullable=False)
    descr = db.Column(db.String(120), unique=True,nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem = db.Column(db.String(120))

usuarios = {
    "user": "1234",
    "admin": "5678"
} 

def autenticar(user, senha):
    if user in usuarios:
        if usuarios[user] == senha:
            return user
    return None
