from db import db #importa o db (banco de dados) do db.py

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    #coluna id sendo definida como primaria
    nome = db.Column(db.String(80), nullable=False)
    #coluna com o nome dos funcionários (limite de string com 80 char)
    cargo = db.Column(db.String(120), nullable=False)
    #coluna com o cargo dos funcionários (limite de string com 120 char)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #coluna com o email dos funcionários, definido como unico (limite de string com 120 char)
    senha = db.Column(db.String(120), unique=True, nullable=False)
    #coluna com a senha dos funcionários sendo definida como unica (limite de string com 120 char)
    cpf = db.Column(db.String(20), unique=True,nullable=False)
    #coluna com o cpf dos funcionários sendo definida como unica (limite de string com 20 char)
    salario = db.Column(db.Float, nullable=False) 
    #coluna com o salario dos funcionários, definido como numero real

class Prato(db.Model):
     id = db.Column(db.Integer, primary_key=True)
    #coluna id sendo definida como primaria
    nome = db.Column(db.String(80), unique=True,nullable=False)
    #coluna com o nome dos pratos (limite de string com 80 char)
    descr = db.Column(db.String(120), unique=True,nullable=False)
    #coluna com a descrição dos pratos (limite de string com 80 char)
    preco = db.Column(db.Float, nullable=False)
    #coluna com o preço dos pratos, definido como real
    imagem = db.Column(db.String(120))
    #coluna com a imagem dos pratos (limite de string com 80 char)

usuarios = {
    "user": "1234",
    "admin": "5678"
} 

def autenticar(user, senha):
    if user in usuarios:
        if usuarios[user] == senha:
            return user
    return None
