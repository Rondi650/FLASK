from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'Rondi'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
 
jogo1 = Jogo("The Legend of Zelda: Breath of the Wild", "Aventura", "Nintendo Switch")
jogo2 = Jogo("God of War Ragnarök", "Ação", "PlayStation 5")
jogo3 = Jogo("Halo Infinite", "FPS", "Xbox Series X")  

lista = [jogo1,jogo2,jogo3]

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('login')    
    return render_template('lista.html', jogos = lista, titulo = 'Jogos')

@app.route('/novo', methods = ['GET'])
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('login')
    return render_template('novo.html', titulo = 'Inserir Novo Jogo')

@app.route('/criar', methods = ['POST'])
def criar_jogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome,categoria,console)
    lista.append(novo_jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if '123' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/novo')
    else:
        flash('Usuario ou senha incorreto.')
        return redirect('/login')
    
@app.route('/logout')
def logout():
     session['usuario_logado'] = None
     flash('Logout efetuado com sucesso!')
     return redirect('/login') 

app.run(host='0.0.0.0', port=8080, debug=True)