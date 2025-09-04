from flask import render_template, redirect, url_for, request, session, flash, send_from_directory
from models import Usuario, Jogo
from database import db
from app import app
from helpers import procurar_capa, deleta_arquivo
import time

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

@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    jogos = Jogo.query.filter_by(id=id).first()   
    
    capa_jogo = procurar_capa(jogos.id)
    
    return render_template('editar.html', titulo='Editando Jogo', jogos = jogos, capa_jogo=capa_jogo)

@app.route('/deletar/<int:id>')
def deletar(id):
    jogo = Jogo.query.filter_by(id=id).first()
    if jogo:
        db.session.delete(jogo)
        db.session.commit()
        flash('Jogo deletado com sucesso')
        deleta_arquivo(jogo.id)
    return redirect(url_for('index'))

@app.route('/atualizar', methods = ['POST'])
def atualizar():
    id = request.form['id']
    jogo = Jogo.query.filter_by(id=id).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']
    db.session.add(jogo)
    db.session.commit()         
    flash('Jogo editado com sucesso!') 

    arquivo = request.files['arquivo']
    timestamp = time.time()
    deleta_arquivo(jogo.id)
    arquivo.save(f'{app.config['UPLOAD_PATH']}\capa{jogo.id}-{timestamp}.jpg')
    
    return redirect(url_for('index'))
    
@app.route('/criar', methods=['POST'])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome=nome, categoria=categoria, console=console)
    db.session.add(jogo)
    db.session.commit()
    flash('Jogo criado com sucesso!')
    
    arquivo = request.files['arquivo']
    timestamp = time.time()
    arquivo.save(f'{app.config['UPLOAD_PATH']}\capa{jogo.id}-{timestamp}.jpg')
    
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

@app.route('/imagem/<nome_arquivo>')
def criar_imagem(nome_arquivo):
    return send_from_directory(app.config['UPLOAD_PATH'],nome_arquivo)