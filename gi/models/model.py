from database import db

# dicionário fake com os usuários e senhas
usuarios = {
    "user": "1234",  # senha do user normal
    "admin": "5678",  # senha do admin
    "funcionario": "9101"  # senha do funcionário
}

# função pra validar login (confere user e senha)
def autenticar(user, senha):
    if user in usuarios:  # checa se o user existe no dicionário
        if usuarios[user] == senha:  # confere se a senha tá certa
            return user  # devolve o user se a autenticação deu certo
    return None  # se não, retorna nada (login inválido)

# classe que mapeia a tabela "prato" no banco de dados
class Prato(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # chave primária (id único)
    nome = db.Column(db.String(100), nullable=False)  # nome do prato
    descricao = db.Column(db.String(255), nullable=False)  # descrição do prato
    preco = db.Column(db.Float, nullable=False)  # preço do prato
    imagem = db.Column(db.String(100), nullable=False)  # caminho ou URL da imagem do prato

    # inicializa os dados do prato
    def __init__(self, nome, descricao, preco, imagem):
        self.nome = nome  # seta o nome
        self.descricao = descricao  # seta a descrição
        self.preco = preco  # seta o preço
        self.imagem = imagem  # seta o caminho da imagem

# classe que mapeia a tabela "funcionario" no banco de dados
class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # chave primária (id único)
    nome = db.Column(db.String(100), nullable=False)  # nome do funcionário
    cargo = db.Column(db.String(100), nullable=False)  # cargo do funcionário
    email = db.Column(db.String(120), nullable=False)
    #coluna com o email dos funcionários, definido como unico (limite de string com 120 char)
    #coluna com o cpf dos funcionários sendo definida como unica (limite de string com 20 char)
    cpf = db.Column(db.String, unique=True, nullable=False)
    salario = db.Column(db.Float, nullable=False) 
    #coluna com o salario dos funcionários, definido como numero real

    # inicializa os dados do funcionário
    def __init__(self, nome, cargo, email, cpf, salario):
        self.nome = nome  # seta o nome
        self.cargo = cargo  # seta o cargo
        self.email = email
        self.cpf = cpf 
        self.salario = salario 


