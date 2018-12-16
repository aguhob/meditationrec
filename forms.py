from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MeditRec(Form):
    stage = StringField('Stage Number: ', validators=[DataRequired("Yo, what stage? Enter a number.")])
    description = StringField('Challenges: ', validators=[DataRequired("Yo, ho'ws it going? Write about it.")])
    submit = SubmitField('Submit')
