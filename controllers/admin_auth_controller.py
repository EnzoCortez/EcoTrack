from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from forms.admin_auth_form import AdminLoginForm
from models.entities import Usuario

admin_auth_bp = Blueprint("admin_auth", __name__, url_prefix="/admin")


# ============================================================
# LOGIN ADMINISTRADOR
# ============================================================
@admin_auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = AdminLoginForm()

    if form.validate_on_submit():
        correo = form.correo.data
        password = form.contrasena.data

        admin = Usuario.query.filter_by(correo=correo, rol="Administrador").first()

        if not admin:
            flash("❌ Este usuario no tiene permisos de administrador.", "danger")
            return render_template("admin/admin_login.html", form=form)

        if not check_password_hash(admin.contrasena, password):
            flash("❌ Contraseña incorrecta.", "danger")
            return render_template("admin/admin_login.html", form=form)

        login_user(admin)
        flash("✔ Bienvenido Administrador.", "success")
        return redirect(url_for("admin.presupuesto"))

    return render_template("admin/admin_login.html", form=form)


# ============================================================
# LOGOUT ADMIN
# ============================================================
@admin_auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión finalizada.", "info")
    return redirect(url_for("admin_auth.login"))
