from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class VincForm(FlaskForm):
    codVinc = IntegerField('Codigo Funcionario x Projeto')
    selectFunc = SelectField(u'Selecione o Funcionario', choices=[('funcionario', 'Funcionarios')])
    selectProj = SelectField(u'Selecione o Projeto', choices=[('projeto', 'Projetos')])
    coordenador = BooleanField('Coordenador')
    salvar = SubmitField('Cadastrar')
    cancelar = SubmitField('Cancelar')
