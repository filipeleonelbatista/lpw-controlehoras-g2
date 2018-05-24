from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    matr = Col('Matricula')
    nome = Col('Nome')
    admin = Col('Admin')

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula')
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 64)])
    admin = BooleanField('Administrador')
    password = PasswordField('Password', validators=[DataRequired()])
    salvar = SubmitField('Cadastrar')
    cancelar = SubmitField('Cancelar')
