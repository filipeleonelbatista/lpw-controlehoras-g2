from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, DateField, DateTimeField, TimeField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired


class lancamentoForm(FlaskForm):
    idLac = HiddenField('ID')
    selectProjeto = SelectField(u'project', validators=[DataRequired()])
    dtInicio = DateTimeField('Data de Inicio', format='%d/%m/%Y')
    hrInicio = DateTimeField('Hora de Inicio', format='%H:%M')
    dtFim = DateTimeField('Data de Termino', format='%d/%m/%Y')
    hrFim = DateTimeField('Data de Termino', format='%H:%M')
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

    def valdDate(__self__, dateInic, dateEnd):
        ret = False
        if dateInic.date() == dateEnd.date():
            if dateInic.time() > dateEnd.time():
                ret = True
        elif dateInic.date() > dateEnd.date():
            ret = True
        return ret
