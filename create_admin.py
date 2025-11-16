from werkzeug.security import generate_password_hash
from app import create_app
from models import db
from models.entities import Usuario

def create_admin_user():
    app = create_app()

    with app.app_context():
        # Comprobar si ya existe un admin
        admin = Usuario.query.filter_by(rol="Administrador").first()
        if admin:
            print("⚠ Ya existe un usuario administrador:")
            print(f"   → {admin.correo}")
            return

        # Datos del admin inicial
        nombre = "Administrador General"
        correo = "admin@ekotrack.com"
        contrasena = "Admin123*"  # puedes cambiarla después
        hashed = generate_password_hash(contrasena)

        nuevo_admin = Usuario(
            nombre=nombre,
            correo=correo,
            contrasena=hashed,
            rol="Administrador"
        )

        db.session.add(nuevo_admin)
        db.session.commit()

        print("✅ Administrador creado exitosamente:")
        print(f"   Usuario: {correo}")
        print(f"   Contraseña: {contrasena}")
        print("   👉 Cambia esta contraseña después de iniciar sesión.")

if __name__ == "__main__":
    create_admin_user()
