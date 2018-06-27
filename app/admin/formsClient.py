from brazilnum.cnpj import validate_cnpj
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ClientsForm(FlaskForm):
	cnpj = StringField(label='CNPJ', validators=[Length(min=14, max=14), DataRequired()])
	nome = StringField(label='Nome', validators=[DataRequired(), Length(1, 64)])
	salvar = SubmitField('Cadastrar')
	cancelar = SubmitField('Cancelar')

	def validacao(__self__, form):
		if (form.cnpj.data == '' or form.nome.data == ''):
			return True
		return False

	def validCnpj(__self__, _cnpj):
		print(_cnpj)
		if validate_cnpj(_cnpj):
			print('Valido')
			return False
		return True
