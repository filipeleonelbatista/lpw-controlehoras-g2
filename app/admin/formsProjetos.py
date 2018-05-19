from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    codProj = Col('CodProj')
    nomeProj = Col('Nome Projeto')
    client = Col('Cliente')
    descricao = Col('Descrição')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))

class ProjetoForm(FlaskForm):
    codProj = IntegerField('Codigo Projeto')
    nomeProj = StringField('Nome do Projeto', validators=[DataRequired(), Length(1, 64)])
    selectClient = SelectField(u'Programming Language', choices=[('cliente', 'Cliente')])
    descrProj = StringField('Descrição do Projeto', validators=[DataRequired(), Length(1, 64)])
    