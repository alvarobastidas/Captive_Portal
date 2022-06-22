from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    movil = StringField('Celular', validators=[DataRequired(), Length(min=10, max=10)])
    submit = SubmitField('Acceder')


class AccessForm(FlaskForm):
    submit = SubmitField('Continuar')