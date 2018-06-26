from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class horasProjetoForm(FlaskForm):
    selectProject = SelectField(u'project', validators=[DataRequired()])
    selectMonth = SelectField(u'lancamento', validators=[DataRequired()])
    gravar = SubmitField('Pesquisar')

