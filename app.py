from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'Rondi'

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
        
usuario1 = Usuario("Bruno Divino", "BD", "alohomora")
usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake", "python_eh_vida")
usuario4 = Usuario('Rondinelle Oliveira','Rondi', '123')

usuarios = { usuario1.nickname :usuario1, 
                usuario2.nickname :usuario2,
                usuario3.nickname :usuario3,
                usuario4.nickname: usuario4}

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
 
jogo1 = Jogo("The Legend of Zelda: Breath of the Wild", "Aventura", "Nintendo Switch")
jogo2 = Jogo("God of War Ragnarök", "Ação", "PlayStation 5")
jogo3 = Jogo("Halo Infinite", "FPS", "Xbox Series X")  

lista = [jogo1,jogo2,jogo3]

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))   
    return render_template('lista.html', jogos = lista, titulo = 'Jogos')

@app.route('/novo', methods = ['GET'])
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('novo.html', titulo = 'Inserir Novo Jogo')

@app.route('/criar', methods = ['POST'])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome,categoria,console)
    lista.append(novo_jogo)
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nickname = request.form['usuario']
    senha = request.form['senha']
    
    if nickname in usuarios:
        usuario = usuarios[nickname]
        if senha == usuario.senha:
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

app.run(host='0.0.0.0', port=8080, debug=True)