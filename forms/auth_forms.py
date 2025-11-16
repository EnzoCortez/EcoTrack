from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    correo = StringField("Correo", validators=[DataRequired(), Email()])
    contrasena = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")


class RegisterForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(min=3)])
    correo = StringField("Correo", validators=[DataRequired(), Email()])
    contrasena = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Registrarse")
