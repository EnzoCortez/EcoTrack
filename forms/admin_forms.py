from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional


class PresupuestoForm(FlaskForm):
    monto_total = DecimalField("Monto total", places=2, validators=[DataRequired()])
    submit = SubmitField("Guardar")


class MatrizForm(FlaskForm):
    id_categoria = SelectField("Categoría", coerce=int, validators=[DataRequired()])
    id_criticidad = SelectField("Criticidad", coerce=int, validators=[DataRequired()])
    puntaje_total = IntegerField(
        "Puntaje total", validators=[DataRequired(), NumberRange(min=1)]
    )
    submit = SubmitField("Guardar Matriz")


class IntervencionForm(FlaskForm):
    id_reporte = SelectField("Reporte", coerce=int, validators=[DataRequired()])
    prioridad = IntegerField("Prioridad", validators=[DataRequired(), NumberRange(min=1)])
    estado = SelectField(
        "Estado",
        choices=[
            ("Pendiente", "Pendiente"),
            ("En Proceso", "En Proceso"),
            ("Completada", "Completada")
        ],
        validators=[DataRequired()],
    )
    fecha_programada = DateField("Fecha programada", validators=[Optional()])
    submit = SubmitField("Guardar Intervención")
