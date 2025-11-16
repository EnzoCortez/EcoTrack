from flask import Flask, render_template
from config import Config
from flask_login import LoginManager
from models.entities import Usuario
from models import db

# Blueprints
from controllers.auth_controller import auth_bp
from controllers.habit_controller import habit_bp
from controllers.admin_controller import admin_bp
from controllers.admin_auth_controller import admin_auth_bp


# --------------------------
# CREATE APP
# --------------------------
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar DB
    db.init_app(app)

    # Inicializar LoginManager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # login de usuarios normales
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_usuario):
        return Usuario.query.get(int(id_usuario))

    # Registrar Blueprints (ORDEN CORRECTO)
    app.register_blueprint(auth_bp)         # login público
    app.register_blueprint(admin_auth_bp)   # login administrador
    app.register_blueprint(admin_bp)        # panel admin
    app.register_blueprint(habit_bp)        # módulo hábitos

    # Ruta principal
    @app.route("/")
    def home():
        return render_template("index.html")

    return app


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
