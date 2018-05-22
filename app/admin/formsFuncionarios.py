from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, PasswordField, IntegerField
=======
from wtforms import StringField, IntegerField
>>>>>>> master
from wtforms.validators import DataRequired, Length
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    matr = Col('Matricula')
<<<<<<< HEAD
    descricao = Col('Descrição')
    senha = Col('Senha')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
=======
    nome = Col('Nome')
>>>>>>> master

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula')
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 64)])
<<<<<<< HEAD
    password = PasswordField('Password', validators=[DataRequired()])
=======
>>>>>>> master
