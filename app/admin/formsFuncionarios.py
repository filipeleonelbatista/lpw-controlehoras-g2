from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length

class FuncionarioForm(FlaskForm):
    matricula = IntegerField('Matricula')
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 64)])
    admin = BooleanField('Administrador')
    password = PasswordField('Password', validators=[DataRequired()])
    salvar = SubmitField('Cadastrar')
    cancelar = SubmitField('Cancelar')
