from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms_components import DateRange
from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    codProj = Col('CodProj')
    nomeProj = Col('Nome Projeto')
    client = Col('Cliente')
    descricao = Col('Descrição')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))

class RelatForm(FlaskForm):
   selectClient = SelectField(u'Clientes', choices=[('cliente', 'Cliente')])
   selectProj = SelectField(u'Projetos', choices=[('projeto', 'Projeto')])
   dateInicial = DateField('Periodo', format="%m/%d/%Y")
   datefinal = DateField(' a ', format="%m/%d/%Y", validators=[DateRange(max=date.today())])
   selectFunc = SelectField(u'Funcionarios', choices=[('funcionario', 'Funcionario')])
   submit = SubmitField('Consult')
