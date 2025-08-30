from flask import Flask, render_template, request, redirect, session, flash, url_for
from conexao_bd import db, Usuario, Jogo, init_app

app = Flask(__name__)
app.secret_key = 'Rondi'

# Inicializa o db com o app
init_app(app)

# Cria as tabelas caso elas nao existam
with app.app_context():
    db.create_all()

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))   
    
    # Buscar jogos - agora com Flask-SQLAlchemy
    jogos = Jogo.query.all()
    
    return render_template('lista.html', jogos=jogos, titulo='Jogos')

@app.route('/novo', methods=['GET'])
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('novo.html', titulo='Inserir Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    # Salvar com Flask-SQLAlchemy
    jogo = Jogo(nome=nome, categoria=categoria, console=console)
    db.session.add(jogo)
    db.session.commit()
    
    flash('Jogo criado com sucesso!')
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nickname = request.form['usuario']
    senha = request.form['senha']
    
    # Buscar com Flask-SQLAlchemy
    usuario = Usuario.query.filter_by(nickname=nickname).first()
    
    if usuario and senha == usuario.senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso')
        return redirect(url_for('novo_jogo'))
    else:
        flash('Usuario ou senha incorreto.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)