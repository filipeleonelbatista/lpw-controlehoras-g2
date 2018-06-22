from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length

class PerfilForm(FlaskForm):
    matricula = IntegerField('Matricula', validators=[DataRequired()])
    nomeCompleto = StringField('Nome completo', validators=[DataRequired(), Length(1, 64)])
    nome = StringField('Nome de usuário', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm = PasswordField('Confirmar senha', validators=[DataRequired()])
    submit = SubmitField('Atualizar')
    cancel = SubmitField('Cancelar')
    upload = SubmitField('Atualizar imagem')
   