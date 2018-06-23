from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length


class AtividadeForm(FlaskForm):
    idAtividade = HiddenField('ID Atividade')
    descricao = StringField(label='Descricao', validators=[DataRequired(), Length(1, 64)])
    salvar = SubmitField('Cadastrar')
    cancelar = SubmitField('Cancelar')

    def validacao(__self__, form):
        if form.descricao.data == '':
            return True
        return False

    def validInteger(__self__, idAtividade):
        if type(idAtividade) == int:
            print('number')
            return False
        return True
