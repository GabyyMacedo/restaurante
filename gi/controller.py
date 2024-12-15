from flask import Blueprint, render_template, request, redirect, url_for, session, flash, json,make_response
from model import *
from repository import PratoRepository, FuncionarioRepository


prato_controllers = Blueprint("prato", __name__)
pratoRepository = PratoRepository()
funcionarioRepository = FuncionarioRepository()

@prato_controllers.before_request
def before_request():
    print(f"Método da Requisição: {request.method} | Caminho da Requisição: {request.path}")

@prato_controllers.after_request
def after_request(response):
    response.set_cookie('visited', 'true')
    return response
@prato_controllers.route("/")
def index():
    listaPratos = Prato.query.all() 
    username = session.get('username')
    visited = request.cookies.get('visited')
    id = request.args.get('id', default=0, type=int)
    cookie = json.loads(request.cookies.get('carrinho', '[]'))

    if id != 0:
        if id in cookie:
            cookie.remove(id)
        else:
            cookie.append(id)

   
    resp = make_response(render_template("index.html", 
                                         listapratos=listaPratos, 
                                         carrinho=cookie))
    resp.set_cookie('carrinho', json.dumps(cookie), max_age=60*60*24)
    return resp

@prato_controllers.route("/sobre")
def sobre():
    return render_template("sobre.html"), 500


@prato_controllers.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']
        
        autenticado = autenticar(user, senha)
        if autenticado:
            session['username'] = user
            flash(f'Bem-vindo, {autenticado}!', 'success')
            return redirect(url_for('prato.welcome'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')  
    return render_template('login.html')

@prato_controllers.route("/welcome")
def welcome():
    username = session.get('username')
    if username == "admin":
        message = "Bem-vindo, ADMIN!"
        return redirect(url_for('prato.listar_funcionarios'))
    elif username == "user":
        message = "Bem-vindo, USER!"
        return redirect(url_for('prato.user',username=username, message=message))
    else:
     message = "Bem-vindo, FUNCIONÁRIO!"
    return redirect(url_for('prato.listar_prato',username=username, message=message))

@prato_controllers.route("/user")
def user():
  
    listaPratos = Prato.query.all()
    carrinho_ids = json.loads(request.cookies.get('carrinho', '[]'))
 
    pratos_no_carrinho = [prato for prato in listaPratos if prato.id in carrinho_ids]
    total_carrinho = sum(prato.preco for prato in pratos_no_carrinho)
    

    return render_template("user.html", listaPratos=pratos_no_carrinho, total=total_carrinho)

@prato_controllers.route("/funcionario")
def listar_prato():
    prato = pratoRepository.get_all_pratos()
    return render_template("funcionario.html", prato=prato)

@prato_controllers.route("/funcionario/add_prato", methods=["POST"])
def add_prato():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = float(request.form["preco"])
    imagem = request.form["imagem"]
    
    pratoRepository.add_prato(nome, descricao, preco, imagem)
    flash('Prato adicionado com sucesso!', 'success')
    return redirect(url_for('prato.index'))

@prato_controllers.route("/funcionario/remove_prato/<int:id>", methods=["POST"])
def remove_prato(id):
    pratoRepository.remove_prato(id)
    flash('Prato removido com sucesso!', 'success')
    return redirect(url_for('prato.index'))

@prato_controllers.route("/admin")
def listar_funcionarios():
    funcionarios = funcionarioRepository.get_all_funcionarios()
    return render_template("admin.html", funcionarios=funcionarios)

@prato_controllers.route("/admin/funcionarios/adicionar", methods=["POST"])
def add_funcionario():
    nome = request.form["nome"]
    cargo = request.form["cargo"]
    
    funcionarioRepository.add_funcionario(nome, cargo)
    flash('Funcionário adicionado com sucesso!', 'success')
    return redirect(url_for('prato.listar_funcionarios'))

@prato_controllers.route("/admin/funcionarios/remover/<int:id>", methods=["POST"])
def remover_funcionario(id):
    funcionarioRepository.remove_funcionario(id)
    flash('Funcionário removido com sucesso!', 'success')
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