from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from functools import wraps
import decimal

from models.entities import (
    PresupuestoMunicipal, Categoria, Criticidad,
    MatrizCriticidad, Reporte, Intervencion
)
from models import db
from forms.admin_forms import PresupuestoForm, MatrizForm, IntervencionForm

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# Middleware de administrador
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.args.get("as_admin") == "1":
            return f(*args, **kwargs)
        flash("Acceso restringido: se requiere rol Administrador.", "danger")
        return redirect(url_for("auth.login"))
    return decorated


# -----------------------------
# PRESUPUESTO
# -----------------------------
@admin_bp.route("/presupuesto", methods=["GET", "POST"])
@admin_required
def presupuesto():
    presupuesto = PresupuestoMunicipal.query.order_by(
        PresupuestoMunicipal.fecha_actualizacion.desc()
    ).first()

    form = PresupuestoForm(obj=presupuesto)

    if form.validate_on_submit():
        try:
            monto = decimal.Decimal(form.monto_total.data)
        except:
            form.monto_total.errors.append("Monto inválido")
            return render_template("admin/admin_presupuesto.html", form=form)

        if monto <= 0:
            form.monto_total.errors.append("El monto debe ser mayor que 0")
            return render_template("admin/admin_presupuesto.html", form=form)

        nuevo = PresupuestoMunicipal(monto_total=monto)
        db.session.add(nuevo)
        db.session.commit()

        flash("Presupuesto actualizado exitosamente", "success")
        return redirect(url_for("admin.presupuesto", as_admin=1))

    return render_template("admin/admin_presupuesto.html", form=form, presupuesto=presupuesto)


# -----------------------------
# MATRIZ
# -----------------------------
@admin_bp.route("/matriz", methods=["GET", "POST"])
@admin_required
def matriz():
    form = MatrizForm()

    form.id_categoria.choices = [
        (c.id_categoria, c.nombre) for c in Categoria.query.order_by(Categoria.nombre)
    ]

    form.id_criticidad.choices = [
        (c.id_criticidad, c.nivel) for c in Criticidad.query.order_by(Criticidad.puntaje.desc())
    ]

    if form.validate_on_submit():
        nueva = MatrizCriticidad(
            id_categoria=form.id_categoria.data,
            id_criticidad=form.id_criticidad.data,
            puntaje_total=form.puntaje_total.data
        )
        db.session.add(nueva)
        db.session.commit()

        flash("Matriz guardada correctamente", "success")
        return redirect(url_for("admin.matriz", as_admin=1))

    matrices = MatrizCriticidad.query.all()
    return render_template("admin/admin_matriz.html", form=form, matrices=matrices)


# -----------------------------
# API REPORTE
# -----------------------------
@admin_bp.route("/api/reporte/<int:id_reporte>")
def api_reporte(id_reporte):
    r = Reporte.query.get_or_404(id_reporte)
    return jsonify({
        "descripcion": r.descripcion,
        "categoria": r.id_categoria,
        "criticidad": r.id_criticidad
    })


# -----------------------------
# INTERVENCIÓN
# -----------------------------
@admin_bp.route("/intervencion", methods=["GET", "POST"])
@admin_required
def intervencion():
    form = IntervencionForm()

    form.id_reporte.choices = [
        (r.id_reporte, f"#{r.id_reporte} - {r.descripcion[:40]}...")
        for r in Reporte.query.order_by(Reporte.fecha_reporte.desc())
    ]

    if form.validate_on_submit():
        nueva = Intervencion(
            id_reporte=form.id_reporte.data,
            prioridad=form.prioridad.data,
            estado=form.estado.data,
            fecha_programada=form.fecha_programada.data
        )
        db.session.add(nueva)
        db.session.commit()

        flash("Intervención registrada.", "success")
        return redirect(url_for("admin.intervencion", as_admin=1))

    return render_template("admin/admin_intervencion.html", form=form)
