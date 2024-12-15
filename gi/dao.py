from model import db, Prato, Funcionario

class PratoDAO:
    
    def add(self, prato):
        db.session.add(prato)
        db.session.commit()

    def remove(self, id):
        prato = Prato.query.get(id)
        if prato:
            db.session.delete(prato)
            db.session.commit()
            return True
        return False

    def get_all(self):
        return Prato.query.all()

    def get_by_id(self, id):
        return Prato.query.get(id)


class FuncionarioDAO:
  
    def add(self, funcionario):
        db.session.add(funcionario)
        db.session.commit()

    def remove(self, id):
        funcionario = Funcionario.query.get(id)
        if funcionario:
            db.session.delete(funcionario)
            db.session.commit()
            return True
        return False

    def get_all(self):
        return Funcionario.query.all()

    def get_by_id(self, id):
        return Funcionario.query.get(id)
