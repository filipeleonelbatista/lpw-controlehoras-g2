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

class horasProjetoForm(FlaskForm):
    selectProject = SelectField(u'project', validators=[DataRequired()])
    selectMonth = SelectField(u'lancamento', validators=[DataRequired()])
    gravar = SubmitField('Pesquisar')

