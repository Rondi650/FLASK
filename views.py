from flask import render_template, redirect, url_for, request, session, flash
from models import Usuario, Jogo
from database import db
from app import app

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))   
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
    jogo = Jogo(nome=nome, categoria=categoria, console=console)
    db.session.add(jogo)
    db.session.commit()
    flash('Jogo criado com sucesso!')
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nickname = request.form['usuario']
    senha = request.form['senha']
    usuario = Usuario.query.filter_by(nickname=nickname).first()
    if usuario and senha == usuario.senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso')
        return redirect(url_for('index'))
    else:
        flash('Usuario ou senha incorreto.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))