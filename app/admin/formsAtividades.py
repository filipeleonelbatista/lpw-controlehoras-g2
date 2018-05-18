from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class AtividadeForm(FlaskForm):
	idAtividade = IntegerField('ID Atividade')
	descricao = StringField(label='Descricao', validators=[DataRequired(), Length(1, 64)])