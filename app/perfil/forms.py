from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length

class PerfilForm(FlaskForm):
    matricula = IntegerField('Matricula', validators=[DataRequired()])
    nomeCompleto = StringField('Nome completo', validators=[DataRequired(), Length(1, 64)])
    nome = StringField('Nome de usuário', validators=[DataRequired(), Length(1, 64)])
    imagem = StringField('Imagem')
    password = PasswordField('Senha', validators=[DataRequired(), Length(4, 64)])
    confirm = PasswordField('Confirmar senha', validators=[DataRequired(), Length(4, 64)])
    submit = SubmitField('Atualizar')
    cancel = SubmitField('Cancelar')
    upload = FileField('Atualizar imagem')
    enviar = SubmitField('Enviar')
    
    def validacao(__self__, form):
    	if form.nomeCompleto.data == '' or form.nome.data == '' or \
    	form.password.data == '' or form.confirm.data == '':
    		return True
    	return False

    def validlengthPass(__self__, form):
    	if (len(form.password.data) >= 4) and (len(form.confirm.data) >= 4):
    		return False
    	return True
   