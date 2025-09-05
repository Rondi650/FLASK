from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', validators=[DataRequired(), length(min=1, max=100)])
    categoria = StringField('Categoria', validators=[DataRequired(), length(min=1, max=50)])
    console = StringField('Console', validators=[DataRequired(), length(min=1, max=50)])
    salvar = SubmitField('Salvar')