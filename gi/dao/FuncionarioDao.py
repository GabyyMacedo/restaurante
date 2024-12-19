from database import db #importa o db (banco de dados) do db.py
from models.model import Funcionario #importa Funcionario do model.py
class FuncionarioDAO:

    # add func no banco
    def add(self, funcionario):
        db.session.add(funcionario)
        db.session.commit()
    # remove func pelo id, se existir
    def remove(self, id):
        funcionario = Funcionario.query.get(id)
        if funcionario:
            db.session.delete(funcionario)
            db.session.commit()
            return True
        return False

    # pega todos os funcs cadastrados
    def get_all(self):
        return Funcionario.query.all()
    # pega func específico pelo id
    def get_by_id(self, id):
        return Funcionario.query.get(id)
    
    def att_funcionario(id, nome, cpf, cargo, salario):
    #atualiza as informações de um funcionario
        funcionario = FuncionarioDAO.get_funcionario(id) #busca o funcionario pelo id
        if funcionario: #se o funcionario for encontrado atualiza as informações:
            funcionario.id=id
            funcionario.nome = nome
            funcionario.cpf=cpf
            funcionario.cargo=cargo
            funcionario.salario=salario
            db.session.commit() #"confirma" a operação
        return funcionario #retorna o funcionario atualizado