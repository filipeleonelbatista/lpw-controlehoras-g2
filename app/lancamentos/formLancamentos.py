from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired, Length

class lancamentoForm(FlaskForm):
    selectProjeto = SelectField(u'project', validators=[DataRequired()])
    dtInicio = DateField('Data de Inicio', format='%Y-%m-%d')
    hrInicio = TimeField('Hora de Inicio')
    dtFim = DateField('Data de Termino')
    hrFim = TimeField('Data de Termino')
    selectAtividade = SelectField(u'project', validators=[DataRequired()])
    descricao = TextAreaField('Descrição do trabalho realizado...')
    gravar = SubmitField('Salvar')


    def validacao(__self__, form):
        return False