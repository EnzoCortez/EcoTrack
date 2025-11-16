from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class AdminLoginForm(FlaskForm):
    correo = StringField("Correo", validators=[DataRequired()])
    contrasena = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")
