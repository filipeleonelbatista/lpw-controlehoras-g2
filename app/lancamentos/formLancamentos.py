from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, DateField, SubmitField, widgets
from wtforms_components import TimeField
from wtforms.validators import DataRequired, Length

class lancamentoForm(FlaskForm):
    selectProjeto = SelectField(u'project', validators=[DataRequired()])
    dtInicio = DateField('Data de Inicio', format='%d/%m/%Y')
    hrInicio = TimeField('Hora de Inicio', format='%H:%M')
    dtFim = DateField('Data de Termino', format='%d/%m/%Y')
    hrFim = TimeField('Data de Termino', format='%H:%M')
    selectAtividade = SelectField(u'project', validators=[DataRequired()])
    descricao = TextAreaField('Descrição do trabalho realizado...')
    gravar = SubmitField('Salvar')


    def validacao(__self__, form):
        return False
