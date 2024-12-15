from db import db
from models.model import Funcionario

class FuncionarioDAO:
    @staticmethod
    def get_funcionario(id):  #busca o funcionário pelo id
        return Funcionario.query.get(id)
        #retorna o funcionario que foi especificado pelo id

    @staticmethod
    def listar_funcionario(): #lista todos os funcionarios
        return Funcionario.query.all()
         #retorna todos os funcionarios cadastrados

    @staticmethod
    def add_funcionario(id, nome, email, cpf, cargo, salario):
        #adiciona um novo funcionario
        funcionario = Funcionario(id=id, nome=nome, email=email,cpf=cpf,cargo=cargo,salario=salario)
        #cria um novo item na classe Funcionario com os parametros passados
        db.session.add(funcionario) #adiciona no banco de dados
        db.session.commit() #"confirma" a operação
        return funcionario #retorna o funcionario que acabou de ser criado

    @staticmethod
    def att_funcionario(id, nome, email, cpf, cargo, salario):
    #atualiza as informações de um funcionario
        funcionario = FuncionarioDAO.get_funcionario(id) #busca o funcionario pelo id
        if funcionario: #se o funcionario for encontrado atualiza as informações:
            funcionario.id=id
            funcionario.nome = nome
            funcionario.email = email
            funcionario.cpf=cpf
            funcionario.cargo=cargo
            funcionario.salario=salario
            db.session.commit() #"confirma" a operação
        return funcionario #retorna o funcionario atualizado

    @staticmethod
    def del_funcionario(id):  #deleta um funcionario
        funcionario = FuncionarioDAO.get_funcionario(id)  #busca o funcionario pelo id
        if funcionario:  #se o funcionario for encontrado
            db.session.delete(funcionario) #deleta o funcionario encontrado do banco de dados
            db.session.commit() #"confirma" a operação
        return funcionario #retorna o funcionario deletado
