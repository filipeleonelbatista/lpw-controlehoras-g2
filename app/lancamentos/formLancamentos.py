from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, DateField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length

class lancamentoForm(FlaskForm):
    selectProjeto = SelectField(u'project', validators=[DataRequired()])
    dtInicio = DateField('Data de Inicio')
    hrInicio = DateTimeField('Hora de Inicio')
    dtFim = DateField('Data de Termino')
    hrFim = DateTimeField('Data de Termino')
    selectAtividade = SelectField(u'project', validators=[DataRequired()])
    descricao = TextAreaField('Descrição do trabalho realizado...')
    iniciar = SubmitField('Iniciar')
    gravar = SubmitField('Gravar')
    parar = SubmitField('Parar')

    def validacao(__self__, form):
        return False