from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

from app.models import Client

class ProjetoForm(FlaskForm):
	codProj = IntegerField('Codigo Projeto')
	nomeProj = StringField('Nome do Projeto', validators=[DataRequired(), Length(1, 64)])
	selectClient = SelectField(u'Cliente', validators=[DataRequired()])
	descrProj = StringField('Descrição do Projeto', validators=[DataRequired(), Length(1, 64)])
	salvar = SubmitField('Cadastrar')
	cancelar = SubmitField('Cancelar')

	def __init__(self, *args, **kwargs):
		super(ProjetoForm, self).__init__(*args, **kwargs)
		self.selectClient.choices = [(a.id, a.nameEmpresa) 
		for a in Client.query.order_by(Client.nameEmpresa)]
