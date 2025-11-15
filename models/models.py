from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Crear la instancia sin inicializar
db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    habits = db.relationship('Habit', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Habit(db.Model):
    __tablename__ = 'habit'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    frequency = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Habit {self.name}>'
