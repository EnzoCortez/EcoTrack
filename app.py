from flask import Flask
from config import Config
from flask_login import LoginManager
from models.entities import Usuario

from models import db
from controllers.auth_controller import auth_bp
from controllers.habit_controller import habit_bp
from controllers.admin_controller import admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(habit_bp)
    app.register_blueprint(admin_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id_usuario):
        return Usuario.query.get(int(id_usuario))