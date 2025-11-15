from flask import Flask
from flask_login import LoginManager
from models.models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecotrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super_secret_key'

# Inicializar base de datos
db.init_app(app)

# Login manager
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Importar blueprints después de crear app
from controllers.auth_controller import auth_bp
from controllers.habit_controller import habit_bp

app.register_blueprint(auth_bp)
app.register_blueprint(habit_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
