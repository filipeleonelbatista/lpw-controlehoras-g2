from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length

class HomeForm(FlaskForm):    
    submit = SubmitField('Projetos')
   