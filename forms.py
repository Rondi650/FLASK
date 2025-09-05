from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', validators=[DataRequired(), length(min=3, max=100)])
    categoria = StringField('Categoria', validators=[DataRequired(), length(min=5, max=50)])
    console = StringField('Console', validators=[DataRequired(), length(min=3, max=50)])
    salvar = SubmitField('Salvar')
    
class FormularioUsuario(FlaskForm):
    nome = StringField('Nome de usuário:', validators=[DataRequired(), length(min=4, max=100)])
    nickname = StringField('Nickname:', validators=[DataRequired(), length(min=3, max=20)])
    senha = PasswordField('Senha:', validators=[DataRequired(), length(min=8, max=100)])
    salvar = SubmitField('Salvar')