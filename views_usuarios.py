from flask import render_template, redirect, url_for, request, session, flash
from models import Usuario
from forms import FormularioUsuario
from app import app


@app.route('/login')
def login():
    form = FormularioUsuario()
    return render_template('login.html',form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    nickname = form.nickname.data
    senha = form.senha.data
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
