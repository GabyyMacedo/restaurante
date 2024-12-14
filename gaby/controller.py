from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response
from models.model import *


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

    if id != 0:
        if id in cookie:
            cookie.remove(id)
        else:
            cookie.append(id)

    # Renderizando com lista de pratos e carrinho
    resp = make_response(render_template("index.html", 
                                         listapratos=listaPratos, 
                                         carrinho=cookie))
    resp.set_cookie('carrinho', json.dumps(cookie), max_age=60*60*24)
    return resp
    return render_template('index.html', username=username, visited=visited)




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
        return redirect(url_for('prato.user',username=username, message=message))
@prato_controllers.route("/user")
def user():
    # Obter o carrinho dos cookies
    carrinho_ids = json.loads(request.cookies.get('carrinho', '[]'))
    
    # Filtrar os pratos que estão no carrinho
    pratos_no_carrinho = [prato for prato in listaPratos if prato.id in carrinho_ids]
    
    # Calcular o preço total
    total_carrinho = sum(prato.preco for prato in pratos_no_carrinho)
    
    # Renderizar o template com os pratos do carrinho e o total
    return render_template("user.html", listaPratos=pratos_no_carrinho, total=total_carrinho, carrinho=carrinho_ids)
# Definindo a lista de funcionários
funcionarios = [
    {"id": 1, "nome": "Giovanna", "cargo": "Gerente"},
    {"id": 2, "nome": "Gaby", "cargo": "Programador"},
    {"id": 3, "nome": "Rafael", "cargo": "Programador"},
    {"id": 4, "nome": "João Amorim ", "cargo": "Garçom"}
]

@prato_controllers.route("/admin")
def listar_funcionarios():
    # Rota para exibir a lista de funcionários
    return render_template("admin.html", funcionarios=funcionarios)

@prato_controllers.route("/admin/funcionarios/adicionar", methods=["POST"])
def adicionar_funcionario():
    global funcionarios
    novo_funcionario = {
        "id": len(funcionarios) + 1,
        "nome": request.form.get("nome"),
        "cargo": request.form.get("cargo")
    }
    funcionarios.append(novo_funcionario)
    flash("Funcionário adicionado com sucesso!", "success")
    return redirect(url_for("prato.listar_funcionarios"))

@prato_controllers.route("/admin/funcionarios/remover/<int:id>", methods=["POST"])
def remover_funcionario(id):
    # Rota para remover um funcionário
    global funcionarios
    funcionarios = [f for f in funcionarios if f["id"] != id]
    flash("Funcionário removido com sucesso!", "success")
    return redirect(url_for("prato.listar_funcionarios"))


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
