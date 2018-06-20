from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, DateField, TimeField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class lancamentoForm(FlaskForm):
    idLac = IntegerField('ID')
    selectProjeto = SelectField(u'project', validators=[DataRequired()])
    dtInicio = DateField('Data de Inicio', format='%d/%m/%Y')
    hrInicio = TimeField('Hora de Inicio', format='%H:%M')
    dtFim = DateField('Data de Termino', format='%d/%m/%Y')
    hrFim = TimeField('Data de Termino', format='%H:%M')
    selectAtividade = SelectField(u'project', validators=[DataRequired()])
    descricao = TextAreaField('Descrição do trabalho realizado...')
    gravar = SubmitField('Salvar')
    salvar = SubmitField('Cadastrar')
    cancelar = SubmitField('Cancelar')

    def validacao(__self__, form):
        if form.dtInicio.data == '' and form.hrInicio.data == ''\
                and form.dtFim.data == '' and form.hrFim.data == '':
            return True
        return False

    def valdDate(__self__, form):
        ret = False
        if form.dtInicio.data == form.dtFim.data:
            if form.hrInicio.data > form.hrFim.data:
                ret = True
        elif form.dtInicio.data > form.dtFim.data:
            ret = True
        return ret
