from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField

class formularioWTF(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='No se puede dejar vacio')])
    correo = EmailField('Email address', [DataRequired(message='No se puede dejar vacio'), Email()])
    boton = SubmitField('Iniciar Sesión')