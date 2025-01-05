from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PredictionForm(FlaskForm):
    customer_data = StringField('Customer Data', validators=[DataRequired()])
    submit = SubmitField('Predict')
