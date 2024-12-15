from database import db

usuarios = {
    "user": "1234",
    "admin": "5678",
    "funcionario":"9101"
}




def autenticar(user, senha):
    if user in usuarios:
        if usuarios[user] == senha:
            return user
    return None



class Prato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, descricao, preco, imagem):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.imagem = imagem

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo