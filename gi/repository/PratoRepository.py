from dao.PratoDao import PratoDAO
from models.model import Prato
#importa PratoDAO de PratoDao.py

class PratoRepository:
    def __init__(self):
        self.dao = PratoDAO()
# cria e add um prato no banco
    def add_prato(self, nome, descricao, preco, imagem):
        prato = Prato(nome=nome, descricao=descricao, preco=preco, imagem=imagem)
        self.dao.add(prato)
 # remove um prato pelo id
    def remove_prato(self, id):
        return self.dao.remove(id)

    def get_all_pratos(self):
        return self.dao.get_all()

    def get_prato_by_id(self, id):
        return self.dao.get_by_id(id)
    