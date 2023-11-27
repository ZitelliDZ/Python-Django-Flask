from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class PersonaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    edad = StringField('Edad',validators=[DataRequired()])
    enviar = SubmitField('Enviar')