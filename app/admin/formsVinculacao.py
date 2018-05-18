from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.validators import DataRequired, Length

class VincForm(FlaskForm):
    codProj = IntegerField('Codigo Funcionario x Projeto')
    selectFunc = SelectField(u'Selecione o Funcionario', choices=[('funcionario')])
    selectProj = SelectField(u'Selecione o Projeto', choices=[('projeto')])
    coordenador = BooleanField('Coordenador')