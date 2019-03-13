from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class sampleForm(FlaskForm):
	title  = StringField('Title')
	detail = TextAreaField('Body')
	submit = SubmitField('Save')