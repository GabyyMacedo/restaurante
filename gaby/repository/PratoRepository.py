from dao.PratoDao import PratoDAO
#importa PratoDAO de PratoDao.py

class PratoRepository:
#classe que vai facilitar a ligaação entre o banco de dados e a utilização das funções
    def __init__(self) -> None:
        self.pratoDao = PratoDAO()
        #inicializa PratoDAO

    def listar_pratos(self):
    #chama o metodo listar_prato e retorna os dados
        return self.pratoDao.listar_pratos()

    def get_prato(self, prato_id):
    #chama o metodo get_prato, passa o id requerido e retorna
        return self.pratoDao.get_prato(prato_id)

    def create_prato(self, prato_id, name, descr, preco):
    #chama o metodo add_prato e passa os dados requeridos e retorna
        return self.pratoDao.add_prato(prato_id, name, descr, preco)

    def update_prato(self, prato_id, name, descr, preco):
    #chama o metodo att_prato e passa os dados requeridos e retorna
        return self.pratoDao.att_prato(prato_id, name, descr, preco)

    def delete_prato(self, prato_id):
    #chama o metodo del_prato e passa os dados requeridos e retorna
        return self.pratoDao.del_prato(prato_id)
