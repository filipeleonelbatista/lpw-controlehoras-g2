from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms import StringField, IntegerField
from wtforms import StringField, IntegerField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    matr = Col('Matricula')
    descricao = Col('Descrição')
    senha = Col('Senha')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    nome = Col('Nome')

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula')
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    admin = BooleanField('Administrador')
    salvar = SubmitField('Cadastrar')
    cancelar = SubmitField('Cancelar')
