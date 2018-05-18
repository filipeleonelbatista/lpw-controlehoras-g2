from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    codFunc = Col('CodFunc')
    descricao = Col('Descrição')
    codProj = Col('Projeto')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))

class VincForm(FlaskForm):
    codProj = IntegerField('Codigo Funcionario x Projeto')
    selectFunc = SelectField(u'Selecione o Funcionario', choices=[('funcionario', 'Funcionarios')])
    selectProj = SelectField(u'Selecione o Projeto', choices=[('projeto', 'Projetos')])
    coordenador = BooleanField('Coordenador')