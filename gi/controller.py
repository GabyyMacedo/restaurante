from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response
from models.model import db, Prato , Funcionario, autenticar #importa o banco de dados, Prato, Funcionario e autenticar
from repository import PratoRepository
from repository import FuncionarioRepository
import json

#cria um blueprint para pratos
prato_controllers = Blueprint("prato", __name__)
pratoRepository = PratoRepository()#repositorio para manipular os dados do prato
funcionarioRepository = FuncionarioRepository()#repositorio pra funcionários
#middleware antes da requisição
@prato_controllers.before_request
def before_request():
    #metodo e caminho de cada requisição
    print(f"Método da Requisição: {request.method} | Caminho da Requisição: {request.path}")
#middleware depois da requisição
@prato_controllers.after_request
#cookie para saber se a pagina ja foi visitada antes
def after_request(response):
    response.set_cookie('visited', 'true')
    return response
#rota inicial
@prato_controllers.route("/")
def index():
    listaPratos = Prato.query.all() #busca os pratos no banco
    username = session.get('username') #recupera o usuario
    visited = request.cookies.get('visited')#ve se ja foi visitado
    id = request.args.get('id', default=0, type=int)
    cookie = json.loads(request.cookies.get('carrinho', '[]'))#cria um carrinho
#adiciona ou tira os pratos do carrinho
    if id != 0:
        if id in cookie:
            cookie.remove(id)
        else:
            cookie.append(id)

    # Renderiza a página e atualiza o carrinho no cookie
    resp = make_response(render_template("index.html", 
                                         listapratos=listaPratos, 
                                         carrinho=cookie))
    #salva o carrinho
    resp.set_cookie('carrinho', json.dumps(cookie), max_age=60*60*24)
    return resp
#rota para ir pra página sobre
@prato_controllers.route("/sobre")
def sobre():
    return render_template("sobre.html")

#rota de login
@prato_controllers.route("/login", methods=['GET', 'POST'])#get pra ver e post pra enviar os dados
def login():
    #pega os dados do forms html
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']
        
        autenticado = autenticar(user, senha)#verifica se tá certo
        if autenticado:
            session['username'] = user
            flash(f'Bem-vindo, {autenticado}!', 'success')#mensagem de bem vindo
            return redirect(url_for('prato.welcome'))#vai pra rota welcome
        else:
            flash('Usuário ou senha inválidos.', 'danger') #não ta certo
    return render_template('login.html')#volta pra fazer login dnv

@prato_controllers.route("/welcome")#rota dps do login
def welcome():
    username = session.get('username')#pega o nome do usuario
    if username == "admin":#verifica se é admin
        message = "Bem-vindo, ADMIN!"
        return redirect(url_for('prato.listar_funcionarios'))#vai pra rota listar funcionário
    elif username == "user":#verifica se é user
        message = "Bem-vindo, USER!"
        return redirect(url_for('prato.user',username=username, message=message))#vai pra rota user
    else:
     message = "Bem-vindo, FUNCIONÁRIO!"#so pode ser funcionario
    return redirect(url_for('prato.listar_prato',username=username, message=message))#vai pra listar prato


@prato_controllers.route("/user")
def user():
    # Obter o carrinho dos cookies
    carrinho_ids = json.loads(request.cookies.get('carrinho', '[]'))
    
    # Filtrar os pratos que estão no carrinho com base no ID
    pratos_no_carrinho = Prato.query.filter(Prato.id.in_(carrinho_ids)).all()
    
    # Calcular o preço total do carrinho
    total_carrinho = sum(prato.preco for prato in pratos_no_carrinho)
    
    # Renderizar a página do usuário com os pratos do carrinho e o total
    return render_template("user.html", listaPratos=pratos_no_carrinho, total=total_carrinho, carrinho=carrinho_ids)


# rota de funcionario
@prato_controllers.route("/funcionario")
def listar_prato():
    prato = pratoRepository.get_all_pratos()  # busca todos os pratos no banco
    return render_template("funcionario.html", prato=prato)


# add um prato (usado no formulário de POST)
@prato_controllers.route("/funcionario/add_prato", methods=["POST"])
def add_prato():
    # pega os dados do formulário
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = float(request.form["preco"])
    imagem = request.form["imagem"]
    
    pratoRepository.add_prato(nome, descricao, preco, imagem)  # salva no banco
    flash('Prato adicionado com sucesso!', 'success')  # mostra mensagem
    return redirect(url_for('prato.index'))  # volta pra página inicial

# remove um prato 
@prato_controllers.route("/funcionario/remover/<int:id>", methods=["POST"])
def remover_prato(id):
    pratoRepository.delete_prato(id)  # apaga do banco pelo ID
    flash('Prato removido com sucesso!', 'success')  # mostra mensagem 
    return redirect(url_for('prato.index'))  # volta pra página inicial
@prato_controllers.route("/admin")
def listar_funcionarios():
    funcionarios = funcionarioRepository.get_all_funcionarios()  # busca todos os funcionários
    return render_template("admin.html", funcionarios=funcionarios)

# add um funcionário 
@prato_controllers.route("/admin/funcionarios/adicionar", methods=["POST"])
def add_funcionario():
    nome = request.form["nome"]  # Nome do funcionário
    cargo = request.form["cargo"] 
    email = request.form["email"]  
    cpf = request.form["cpf"]   # Cargo dele
    salario = request.form["salario"]  
    
    funcionarioRepository.add_funcionario(nome, cargo, email, cpf, salario)  # Salva no banco
    flash('Funcionário adicionado com sucesso!', 'success')  # Mostra mensagem
    return redirect(url_for('prato.listar_funcionarios'))

# remove um funcionário 
@prato_controllers.route("/admin/funcionarios/remover/<int:id>", methods=["POST"])
def remover_funcionario(id):
    funcionarioRepository.remove_funcionario(id)  # apaga pelo ID
    flash('Funcionário removido com sucesso!', 'success')  # Mostra msg
    return redirect(url_for('prato.listar_funcionarios'))

@prato_controllers.route("/logout")
def logout():
    session.pop('username', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('prato.login'))

@prato_controllers.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

@prato_controllers.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

@prato_controllers.errorhandler(401)
def unauthorized(e):
    return render_template("401.html"), 401

@prato_controllers.errorhandler(500)
def serverError(e):
    return render_template("500.html"), 500
