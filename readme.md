# Jogoteca Flask

Este é um projeto de estudo usando Flask, SQLAlchemy, Flask-WTF e Bootstrap para gerenciar jogos e usuários, com upload de imagens de capa.

## Funcionalidades

- Cadastro, edição e exclusão de jogos
- Cadastro e autenticação de usuários
- Upload de imagens de capa para cada jogo
- Proteção CSRF e senhas seguras com Bcrypt
- Interface responsiva com Bootstrap

## Estrutura de pastas

```
├── app.py
├── config.py
├── database.py
├── models.py
├── forms.py
├── helpers.py
├── views_jogo.py
├── views_usuarios.py
├── templates/
│   ├── template.html
│   ├── novo.html
│   ├── editar.html
│   ├── lista.html
│   ├── login.html
│   ├── usuario.html
├── static/
│   ├── style.css
│   ├── bootstrap.css
├── uploads/
│   └── (imagens de capa)
```

## Como rodar

1. Instale as dependências:
   ```
   pip install flask flask_sqlalchemy flask_wtf flask-bcrypt
   ```
2. Execute o projeto:
   ```
   python app.py
   ```
3. Acesse `http://localhost:5000` no navegador.

## Observações

- A pasta `uploads` é criada automaticamente para armazenar as imagens.
- As senhas dos usuários são salvas com hash para segurança.
- O projeto é apenas para fins de estudo e pode ser expandido