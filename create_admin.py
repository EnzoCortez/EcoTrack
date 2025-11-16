from app import create_app
from models import db
from models.entities import Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    correo = "admin@ekotrack.com"
    admin = Usuario.query.filter_by(correo=correo).first()

    if not admin:
        new_admin = Usuario(
            nombre="Administrador General",
            correo=correo,
            contrasena=generate_password_hash("admin1234"),
            rol="Administrador"
        )
        db.session.add(new_admin)
        db.session.commit()
        print("Administrador creado correctamente.")
    else:
        print("El administrador ya existe.")
