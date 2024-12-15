from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        
        from model import Prato, Funcionario
       
        if Prato.query.count() == 0: 
            prato1 = Prato(nome="Carne Argentina", descricao="Prato suculento e macio, preparado com cortes selecionados e temperos especiais, para uma experiência saborosa e intensa.", preco=89.90, imagem="gallery5.jpg")
            prato2 = Prato(nome="Hamburguer", descricao="Um sanduíche suculento com carne grelhada, queijo e acompanhamentos variados.", preco=35.90, imagem="hamburguer.jpg")
            prato3 = Prato(nome="Frango", descricao="Peito ou coxa de frango suculenta, assada ou grelhada, com temperos que destacam o sabor caseiro e aconchegante.", preco=45.90, imagem="menu3.jpg")
            prato4=Prato(nome= "Caipirinha",descricao=" O clássico brasileiro, feito com cachaça, limão e açúcar, trazendo um equilíbrio entre doce e azedo.",preco=35.00, imagem="drink1.jpg")
            prato5=Prato (nome="Fettucinne",descricao=" Cremoso e cheio de sabor, o fettucine é preparado com arroz arbóreo e ingredientes frescos, criando uma combinação irresistível.",preco=58.00, imagem="macarrao.jpg")
            prato6=Prato(nome="Salmão",descricao="Peixe nobre, levemente grelhado ou assado, com uma crosta dourada e interior macio, perfeito para um toque gourmet.",preco=75.00, imagem="peixe.jpg")
            prato7=Prato(nome="Margarita",descricao=" Combinação refrescante de tequila, limão e licor de laranja, perfeita para quem busca um toque cítrico e vibrante.",preco=25.00, imagem="drink2.jpg")
            prato8=Prato(nome="Suco",descricao=" Suco Natural de sabores diversos.",preco=10.00,imagem= "drink3.jpg")
            prato9=Prato(nome="Carne",descricao="Corte nobre de carne, suculento e perfeitamente temperado, grelhado ou assado para realçar seu sabor intenso e macio",preco=78.00,imagem="menu9.jpg")
            prato10=Prato(nome="Feijoada",descricao=" Um clássico brasileiro feito com feijão preto e carnes, servido com arroz e farofa.",preco=66.00,imagem= "feijoada.jpg")
            prato11=Prato(nome="Torta",descricao="Sobremesa delicada com recheio cremoso, perfeita para adoçar o dia.",preco=20.00,imagem= "torta.jpg")
            prato12=Prato(nome="Brownie",descricao=" Um bolo denso e irresistível de chocolate, com textura macia e sabor intenso.",preco=12.00,imagem= "brownie.jpg")

            db.session.add(prato1)
            db.session.add(prato2)
            db.session.add(prato3)
            db.session.add(prato4)
            db.session.add(prato5)
            db.session.add(prato6)
            db.session.add(prato7)
            db.session.add(prato8)
            db.session.add(prato9)
            db.session.add(prato10)
            db.session.add(prato11)
            db.session.add(prato12)

            db.session.commit()


        if Funcionario.query.count() == 0:
            funcionario1 = Funcionario(nome="Giovanna", cargo="Gerente")
            funcionario2 = Funcionario(nome="Gaby", cargo="Programador")
            funcionario3 = Funcionario(nome="Rafael", cargo="Programador")
            db.session.add(funcionario1)
            db.session.add(funcionario2)
            db.session.add(funcionario3)
            db.session.commit()