from datetime import datetime, date
from flask_login import UserMixin
from models import db


class Usuario(UserMixin, db.Model):
    __tablename__ = "Usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(200), unique=True, nullable=False)
    contrasena = db.Column(db.String(500), nullable=False)
    rol = db.Column(db.String(50), default="Usuario")
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        """Flask-Login necesita esto para identificar al usuario."""
        return str(self.id_usuario)


class Categoria(db.Model):
    __tablename__ = "Categoria"
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    nivel_base_criticidad = db.Column(db.String(20), nullable=False)


class Criticidad(db.Model):
    __tablename__ = "Criticidad"
    id_criticidad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nivel = db.Column(db.String(20), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)


class Reporte(db.Model):
    __tablename__ = "Reporte"
    id_reporte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.Text, nullable=False)
    ubicacion = db.Column(db.String(255))
    fecha_reporte = db.Column(db.DateTime, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey("Usuario.id_usuario"))
    id_categoria = db.Column(db.Integer, db.ForeignKey("Categoria.id_categoria"))
    id_criticidad = db.Column(db.Integer, db.ForeignKey("Criticidad.id_criticidad"))
    evidencia_url = db.Column(db.String(255))


class MatrizCriticidad(db.Model):
    __tablename__ = "MatrizCriticidad"
    id_matriz = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey("Categoria.id_categoria"))
    id_criticidad = db.Column(db.Integer, db.ForeignKey("Criticidad.id_criticidad"))
    puntaje_total = db.Column(db.Integer, nullable=False)


class PresupuestoMunicipal(db.Model):
    __tablename__ = "PresupuestoMunicipal"
    id_presupuesto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monto_total = db.Column(db.Numeric(12, 2), nullable=False)
    fecha_actualizacion = db.Column(db.Date, default=date.today)


class Intervencion(db.Model):
    __tablename__ = "Intervencion"
    id_intervencion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_reporte = db.Column(db.Integer, db.ForeignKey("Reporte.id_reporte"))
    prioridad = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), default="Pendiente")
    fecha_programada = db.Column(db.Date)
