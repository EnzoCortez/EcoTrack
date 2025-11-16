from models import db
from flask_login import UserMixin
from datetime import datetime


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(200), unique=True, nullable=False)
    contrasena = db.Column(db.String(500), nullable=False)
    rol = db.Column(db.String(50), default="Ciudadano")
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        return str(self.id_usuario)


class Categoria(db.Model):
    __tablename__ = "categoria"

    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    nivel_base_criticidad = db.Column(db.String(10), nullable=False)


class Criticidad(db.Model):
    __tablename__ = "criticidad"

    id_criticidad = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.String(10), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)


class Reporte(db.Model):
    __tablename__ = "reporte"

    id_reporte = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=False)
    ubicacion = db.Column(db.String(255))
    fecha_reporte = db.Column(db.DateTime, default=datetime.utcnow)

    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id_usuario"))
    id_categoria = db.Column(db.Integer, db.ForeignKey("categoria.id_categoria"))
    id_criticidad = db.Column(db.Integer, db.ForeignKey("criticidad.id_criticidad"))

    evidencia_url = db.Column(db.String(255))


class MatrizCriticidad(db.Model):
    __tablename__ = "matriz_criticidad"

    id_matriz = db.Column(db.Integer, primary_key=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey("categoria.id_categoria"))
    id_criticidad = db.Column(db.Integer, db.ForeignKey("criticidad.id_criticidad"))
    puntaje_total = db.Column(db.Integer, nullable=False)


class PresupuestoMunicipal(db.Model):
    __tablename__ = "presupuesto_municipal"

    id_presupuesto = db.Column(db.Integer, primary_key=True)
    monto_total = db.Column(db.Numeric(12, 2), nullable=False)
    fecha_actualizacion = db.Column(db.Date, default=datetime.utcnow)


class Intervencion(db.Model):
    __tablename__ = "intervencion"

    id_intervencion = db.Column(db.Integer, primary_key=True)
    id_reporte = db.Column(db.Integer, db.ForeignKey("reporte.id_reporte"), nullable=False)
    prioridad = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), default="Pendiente")
    fecha_programada = db.Column(db.Date)
