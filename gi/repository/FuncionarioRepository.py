from dao import FuncionarioDAO
from models.model import Funcionario
#importa FuncionarioDAO de Funcionario.py

class FuncionarioRepository:
    def __init__(self):
        self.dao = FuncionarioDAO()
# cria e add um func no banco
    def add_funcionario(self, nome, cargo, email, cpf, salario):
        funcionario = Funcionario(nome=nome, cargo=cargo, email= email, cpf=cpf, salario= salario)
        self.dao.add(funcionario)
#faz as mesmas coisas com o funcionario
    def remove_funcionario(self, id):
        return self.dao.remove(id)

    def get_all_funcionarios(self):
        return self.dao.get_all()

    def get_funcionario_by_id(self, id):
        return self.dao.get_by_id(id)