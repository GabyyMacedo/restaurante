from dao.FuncionarioDao import FuncionarioDAO
#importa FuncionarioDAO de Funcionario.py

class FuncionarioRepository:
#classe que vai facilitar a ligaação entre o banco de dados e a utilização das funções
    def __init__(self) -> None:
        self.funcionarioDao = FuncionarioDAO()
        #inicializa funcionarioDAO

    def listar_funcionario(self):
    #chama o metodo listar_funcionario e retorna os dados
        return self.funcionarioDao.listar_funcionarios()

    def get_funcionario(self, id):
    #chama o metodo get_funcionario, passa o id requerido e retorna
        return self.funcionarioDao.get_funcionario(id)

    def create_funcionario(self, id, nome, cpf, cargo, salario):
    #chama o metodo add_funcionario e passa os dados requeridos e retorna
        return self.funcionarioDao.add_funcionario(id, nome, cpf, cargo, salario)

    def update_funcionario(self,id, nome, cpf, cargo, salario):
    #chama o metodo att_funcionario e passa os dados requeridos e retorna
        return self.funcionarioDao.att_funcionario(id, nome, cpf, cargo, salario)

    def delete_funcionario(self, id):
    #chama o metodo del_funcionario e passa os dados requeridos e retorna
        return self.funcionarioDao.del_funcionario(id)
