from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    cnpj = Col('CNPJ/CPF')
    nome = Col('Nome')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))

class ClientsForm(FlaskForm):
	cnpj = StringField(label='CNPJ', validators=[Length(min=14, max=14), DataRequired()])
	nome = StringField(label='Nome', validators=[DataRequired(), Length(1, 64)])