from flask import Flask, render_template, request, redirect, session, flash, url_for

# obrigatorio para iniciar o Flask
app = Flask(__name__)
# sem o secret key, o session(cookie), nao funciona
app.secret_key = 'Rondi'

# Classe jogo para instanciar objetos
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
 
# instanciado jogos padrao ja que nao tem banco de dados
jogo1 = Jogo("The Legend of Zelda: Breath of the Wild", "Aventura", "Nintendo Switch")
jogo2 = Jogo("God of War Ragnarök", "Ação", "PlayStation 5")
jogo3 = Jogo("Halo Infinite", "FPS", "Xbox Series X")  

# lista com os jogos da classe, tem que estar do lado de fora para ser global
lista = [jogo1,jogo2,jogo3]

 # pagina de login
@app.route('/login')
def login():
    # sempre direciona para a pagina login.html
    return render_template('login.html')

 # pagina com a tabela de jogos, interface vem da tabela lista.html
@app.route('/')
def index():
    # SE cookie vazio, pagina nao entra | TEM que estar logado
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # volta para a pagina de login
        return redirect(url_for('login'))   
    # cookie com nome de usuario == True | direciona para pagina com a tabela de jogos
    return render_template('lista.html', jogos = lista, titulo = 'Jogos')

 # pagina para criar os jogos, interface vem da tabela movo.html
@app.route('/novo', methods = ['GET'])
def novo_jogo():
    # SE cookie vazio, pagina nao entra | TEM que estar logado
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # volta para a pagina de login
        return redirect(url_for('login'))
    # cookie com nome de usuario == True | direciona para pagina de criar jogos
    return render_template('novo.html', titulo = 'Inserir Novo Jogo')

# pagina de redirecionamento | recebe dados da pagina de criar jogos | Apenas uma ponte que leva para a pagina com a tabela
# dados vem do formulario da pagina novo.html
@app.route('/criar', methods = ['POST'])
def criar_jogo():
    # vai no html e pega os dados do input
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    # instancia a classe baseado nos inputs recebidos do HTML
    novo_jogo = Jogo(nome,categoria,console)
    # inclui os dados do input na lista
    lista.append(novo_jogo)
    # direciona para a pagina da tabela ja com o novo jogo adicionado
    return redirect(url_for('index'))

# pagina de validacao de login | dados vem do formulario da pagina login.html
@app.route('/autenticar', methods=['POST'])
def autenticar():
    # SE a senha estiver correta
    if '123' == request.form['senha']:
        # session == cookie | recebe o nome do usuario conforme input da pagina de login
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        # direciona para a pagina de criar jogos
        return redirect(url_for('novo_jogo'))
    else:
        flash('Usuario ou senha incorreto.')
        # SE a senha estiver errada, volta eternamente para a pagina de login
        return redirect(url_for('index'))
    
# pagina de logout, desativa os cookies
@app.route('/logout')
def logout():
    # apaga os cookies da funcao session
     session['usuario_logado'] = None
     flash('Logout efetuado com sucesso!')
     # volta para a pagina de login
     return redirect(url_for('login'))

app.run(host='0.0.0.0', port=8080, debug=True)