from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    codAtiv = Col('CodAtividade')
    descricao = Col('Descrição')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))

class AtividadeForm(FlaskForm):
	idAtividade = IntegerField('ID Atividade')
	descricao = StringField(label='Descricao', validators=[DataRequired(), Length(1, 64)])