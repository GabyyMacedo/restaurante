from database import db #importa o db (banco de dados) do db.py
from models.model import Prato #importa Prato do model.py

class PratoDAO:
    
    # add prato no banco
    def add(self, prato):
        db.session.add(prato)
        db.session.commit()

    # remove prato pelo id, se achar
    def remove(self, id):
        prato = Prato.query.get(id)
        if prato:
            db.session.delete(prato)
            db.session.commit()
            return True
        return False

    # pega todos os pratos cadastrados
    def get_all(self):
        return Prato.query.all()

    # pega prato específico pelo id
    def get_by_id(self, id):
        return Prato.query.get(id)

