from flask import render_template, redirect, url_for, request, session, flash
from models import Usuario
from forms import FormularioUsuario
from app import app
from database import db
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    form = FormularioUsuario()
    return render_template('login.html',form=form)


@app.route('/criar_usuario')
def criar_usuario():
    form = FormularioUsuario()
    return render_template('usuario.html', form=form)


@app.route('/novo_usuario', methods=['POST'])
def novo_usuario():
    form = FormularioUsuario(request.form)
    
    if not form.validate_on_submit():
        return redirect(url_for('index'))

    return(redirect(url_for('index')))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    nickname = form.nickname.data
    usuario = Usuario.query.filter_by(nickname=nickname).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
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

        
