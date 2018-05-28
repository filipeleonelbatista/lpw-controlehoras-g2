from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class AtividadeForm(FlaskForm):
	idAtividade = IntegerField('ID Atividade')
	descricao = StringField(label='Descricao', validators=[DataRequired(), Length(1, 64)])
	salvar = SubmitField('Cadastrar')
	cancelar = SubmitField('Cancelar')
	