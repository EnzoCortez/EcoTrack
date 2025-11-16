from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from forms.auth_forms import LoginForm, RegisterForm
from models.entities import Usuario
from models import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        correo = form.correo.data
        contrasena = form.contrasena.data

        user = Usuario.query.filter_by(correo=correo).first()

        if user and check_password_hash(user.contrasena, contrasena):
            login_user(user)
            flash("Bienvenido", "success")
            return redirect(url_for("habit.dashboard"))
        else:
            flash("Correo o contraseña incorrectos", "danger")

    return render_template('login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        nuevo = Usuario(
            nombre=form.nombre.data,
            correo=form.correo.data,
            contrasena=generate_password_hash(form.contrasena.data)
        )
        db.session.add(nuevo)
        db.session.commit()

        flash("Registro exitoso.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
