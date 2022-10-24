from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddCarForm(FlaskForm):
    name = StringField('Model:', validators=[DataRequired()])
    year = StringField('Year: ', validators=[DataRequired()])
    origin = StringField('Origin: ', validators=[DataRequired()])
    mpg = StringField('Miles Per Gallon (MPG): ', validators=[DataRequired()])
    submit = SubmitField('Save')

class SearchForm(FlaskForm):
    name = StringField('Model:', validators=[DataRequired()])
    submit = SubmitField('Search')


