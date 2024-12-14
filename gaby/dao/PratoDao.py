from database import db
from models.model import Prato, db

class PratoDAO:
    @staticmethod
    def get_prato(id): #busca o prato pelo id
        return Prato.query.get(id)
        #retorna o prato que foi especificado pelo id

    @staticmethod
    def listar_pratos(): #lista todos os pratos
        return Prato.query.all()
        #retorna todos os pratos cadastrados

    @staticmethod
    def add_prato(id, name, descr, preco):
    #adiciona um novo prato
        prato = Prato(id=id, name=name, descr=descr, preco=preco)
        #cria um novo item na classe Prato com os parametros passados
        db.session.add(prato) #adiciona no banco de dados
        db.session.commit() #"confirma" a operação
        return prato #retorna o prato que acabou de ser criado

    @staticmethod
    def att_prato(id, name, descr, preco):
    #atualiza as informações de um prato
        prato = PratoDAO.get_prato(id) #busca o prato pelo id
        if prato: #se o prato for encontrado atualiza as informações:
            prato.id = id
            prato.name = name
            prato.descr = descr
            prato.preco = preco
            db.session.commit() #"confirma" a operação
        return prato #retorna o prato atualizado

    @staticmethod
    def del_prato(id): #deleta um prato
        prato = PratoDAO.get_prato(id) #busca o prato pelo id
        if prato: #se o prato for encontrado
            db.session.delete(prato) #deleta o prato encontrado do banco de dados
            db.session.commit() #"confirma" a operação
        return prato #retorna o prato deletado
