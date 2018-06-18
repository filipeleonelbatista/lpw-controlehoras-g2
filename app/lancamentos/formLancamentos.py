from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, DateField, TimeField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from wtforms_components import read_only

class lancamentoForm(FlaskForm):
    idLac = IntegerField('ID')
    selectProjeto = SelectField(u'project', validators=[DataRequired()])
    dtInicio = DateField('Data de Inicio', format='%d/%m/%Y')
    hrInicio = TimeField('Hora de Inicio')
    dtFim = DateField('Data de Termino', format='%d/%m/%Y')
    hrFim = TimeField('Data de Termino')
    selectAtividade = SelectField(u'project', validators=[DataRequired()])
    descricao = TextAreaField('Descrição do trabalho realizado...')
    gravar = SubmitField('Salvar')
    salvar = SubmitField('Cadastrar')
    cancelar = SubmitField('Cancelar')

    def validacao(__self__, form):
        return False
