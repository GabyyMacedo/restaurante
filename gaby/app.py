from flask import Flask
from database import init_db
from repository.PratoRepository import PratoRepository
from repository.FuncionarioRepository import FuncionarioRepository
from controller import prato_controllers
from models.model import db, Prato
#importa db e Prato do arquivo model

app = Flask(__name__)
app.register_blueprint(prato_controllers)

pratoRepository=PratoRepository()
funcionarioRepository = FuncionarioRepository()
app.secret_key = 'sua_chave_secreta_aqui' 

pratos_iniciais = [ #pratos pré-adicionados no banco de dados
    {"id": 1, "nome": "Carne Argentina", "descricao": "Prato suculento e macio, preparado com cortes selecionados e temperos especiais, para uma experiência saborosa e intensa.", "preco": 89.00, "imagem": "gallery5.jpg"},
    {"id": 2, "nome": "Hamburguer", "descricao": "Um sanduíche suculento com carne grelhada, queijo e acompanhamentos variados.", "preco": 35.00, "imagem": "hamburguer.jpg"},
    {"id": 3, "nome": "Frango", "descricao": "Peito ou coxa de frango suculenta, assada ou grelhada, com temperos que destacam o sabor caseiro e aconchegante.", "preco": 45.00, "imagem": "menu3.jpg"},
    {"id": 4, "nome": "Caipirinha", "descricao": "O clássico brasileiro, feito com cachaça, limão e açúcar, trazendo um equilíbrio entre doce e azedo.", "preco": 35.00, "imagem": "drink1.jpg"},
    {"id": 5, "nome": "Fettucinne", "descricao": "Cremoso e cheio de sabor, o fettucine é preparado com arroz arbóreo e ingredientes frescos, criando uma combinação irresistível.", "preco": 58.00, "imagem": "macarrao.jpg"},
    {"id": 6, "nome": "Salmão", "descricao": "Peixe nobre, levemente grelhado ou assado, com uma crosta dourada e interior macio, perfeito para um toque gourmet.", "preco": 75.00, "imagem": "peixe.jpg"},
    {"id": 7, "nome": "Margarita", "descricao": "Combinação refrescante de tequila, limão e licor de laranja, perfeita para quem busca um toque cítrico e vibrante.", "preco": 25.00, "imagem": "drink2.jpg"},
    {"id": 8, "nome": "Suco", "descricao": "Suco Natural de sabores diversos.", "preco": 10.00, "imagem": "drink3.jpg"},
    {"id": 9, "nome": "Carne", "descricao": "Corte nobre de carne, suculento e perfeitamente temperado, grelhado ou assado para realçar seu sabor intenso e macio.", "preco": 78.00, "imagem": "menu9.jpg"},
    {"id": 10, "nome": "Feijoada", "descricao": "Um clássico brasileiro feito com feijão preto e carnes, servido com arroz e farofa.", "preco": 66.00, "imagem": "feijoada.jpg"},
    {"id": 11, "nome": "Torta", "descricao": "Sobremesa delicada com recheio cremoso, perfeita para adoçar o dia.", "preco": 20.00, "imagem": "torta.jpg"},
    {"id": 12, "nome": "Brownie", "descricao": "Um bolo denso e irresistível de chocolate, com textura macia e sabor intenso.", "preco": 12.00, "imagem": "brownie.jpg"}
]

def inserir_dados_iniciais():
#insere os dados no banco
    for prato in pratos_iniciais:
    #percorre os pratos
        if not Prato.query.filter_by(id=prato["id"]).first():  
            #verifica se ja existe um prato com o mesmo id
            novo_prato = Prato(id=prato["id"], nome=prato["nome"], descricao=prato["descricao"], preco=prato["preco"], imagem=prato["imagem"])
            #cria um novo prato com os dados pré-fornecidos
            db.session.add(novo_prato)
            #add o prato no banco de dados
    db.session.commit() #confirma a operação

inserir_dados_iniciais()
#insere dados automaticamente quando a aplicação


if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)
