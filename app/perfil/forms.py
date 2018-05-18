from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Length

class PerfilForm(FlaskForm):
    matricula = IntegerField('Matricula', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Save')
   