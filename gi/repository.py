from dao import PratoDAO, FuncionarioDAO
from model import Prato, Funcionario

class PratoRepository:
    def __init__(self):
        self.dao = PratoDAO()

    def add_prato(self, nome, descricao, preco, imagem):
        prato = Prato(nome=nome, descricao=descricao, preco=preco, imagem=imagem)
        self.dao.add(prato)

    def remove_prato(self, id):
        return self.dao.remove(id)

    def get_all_pratos(self):
        return self.dao.get_all()

    def get_prato_by_id(self, id):
        return self.dao.get_by_id(id)


class FuncionarioRepository:
    def __init__(self):
        self.dao = FuncionarioDAO()

    def add_funcionario(self, nome, cargo):
        funcionario = Funcionario(nome=nome, cargo=cargo)
        self.dao.add(funcionario)

    def remove_funcionario(self, id):
        return self.dao.remove(id)

    def get_all_funcionarios(self):
        return self.dao.get_all()

    def get_funcionario_by_id(self, id):
        return self.dao.get_by_id(id)
