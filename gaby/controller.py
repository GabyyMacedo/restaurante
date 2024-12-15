from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response
from models.model import db, Prato , Funcionario, autenticar #importa o banco de dados, Prato, Funcionario e autenticar
import json

prato_controllers = Blueprint("prato", __name__)

@prato_controllers.before_request
def before_request():
    print(f"Método da Requisição: {request.method} | Caminho da Requisição: {request.path}")

@prato_controllers.after_request
def after_request(response):
    response.set_cookie('visited', 'true')
    return response

@prato_controllers.route("/")
def index():
    username = session.get('username')
    visited = request.cookies.get('visited')
    id = request.args.get('id', default=0, type=int)
    cookie = json.loads(request.cookies.get('carrinho', '[]'))

    listaPratos = Prato.query.all() #busca todos os pratos no banco de dados

    #verifica por meio de cookie se o id do produto ja está no carrinho
    if id != 0:
        if id in cookie:
            cookie.remove(id)
        else:
            cookie.append(id)

    #busca todos os pratos no banco de dados
    pratos = Prato.query.all()

    #mostra a página com a lista de pratos e o carrinho
    resp = make_response(render_template("index.html", 
                                         listaPratos=listaPratos, 
                                         carrinho=cookie))
    resp.set_cookie('carrinho', json.dumps(cookie), max_age=60*60*24)
    return resp

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
    else:
        message = "Bem-vindo, USER!"
        return redirect(url_for('prato.user', username=username, message=message))

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


@prato_controllers.route("/admin")
def listar_funcionarios():
    funcionarios = Funcionario.query.all()  #busca todos os funcionários no banco de dados
    return render_template("admin.html", funcionarios=funcionarios)


@prato_controllers.route("/admin/funcionarios/adicionar", methods=["POST"])
def adicionar_funcionario():
    nome = request.form.get("nome")
    cargo = request.form.get("cargo")
    email = request.form.get("email")
    cpf = request.form.get("cpf")
    senha = request.form.get("senha")
    salario = float(request.form.get("salario"))

    if Funcionario.query.filter_by(email=email).first() or Funcionario.query.filter_by(cpf=cpf).first():
    #verifica se o email ou CPF já estão cadastrados
        flash("Email ou CPF já cadastrados.", "danger")
        return redirect(url_for("prato.listar_funcionarios"))

    novo_funcionario = Funcionario(
    #cria o novo funcionário e adiciona no banco de dados
        nome=nome,
        cargo=cargo,
        email=email,
        cpf=cpf,
        senha=senha,
        salario=salario
    )
    db.session.add(novo_funcionario) 
    db.session.commit()

    flash("Funcionário adicionado com sucesso!", "success")
    return redirect(url_for("prato.listar_funcionarios"))

@prato_controllers.route("/admin/funcionarios/remover/<int:id>", methods=["POST"])
def remover_funcionario(id):
    funcionario = Funcionario.query.get(id) #pega pelo id
    if funcionario:
        db.session.delete(funcionario)
        db.session.commit()
        flash("Funcionário removido com sucesso!", "success")
    else:
        flash("Funcionário não encontrado.", "danger")
    return redirect(url_for("prato.listar_funcionarios"))

@prato_controllers.route("/admin/pratos/adicionar", methods=["POST"])
def adicionar_prato():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    preco = float(request.form.get("preco"))
    imagem = request.form.get("imagem")

    if Prato.query.filter_by(nome=nome).first():
    #verifica se o prato já existe no banco de dados
        flash("Prato já cadastrado.", "danger")
        return redirect(url_for("prato.index"))

    novo_prato = Prato(
    #cria o novo prato e adiciona no banco de dados
        nome=nome,
        descricao=descricao,
        preco=preco,
        imagem=imagem
    )
    db.session.add(novo_prato)
    db.session.commit()

    flash("Prato adicionado com sucesso!", "success")
    return redirect(url_for("prato.index"))

@prato_controllers.route("/admin/pratos/remover/<int:id>", methods=["POST"])
def remover_prato(id): #pega pelo id
    prato = Prato.query.get(id)
    if prato:
        db.session.delete(prato)
        db.session.commit()
        flash("Prato removido com sucesso!", "success")
    else:
        flash("Prato não encontrado.", "danger")
    return redirect(url_for("prato.index"))


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
