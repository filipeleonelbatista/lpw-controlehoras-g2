from flask_wtf import FlaskForm
from wtforms import StringField

class ClientsForm(FlaskForm):
	cnpj = StringField(label='CNPJ', validators=[Length(min=14, max=14), DataRequired()])
	nome = StringField(label='Nome', validators=[DataRequired(), Length(1, 64)])