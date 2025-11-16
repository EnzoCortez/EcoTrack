import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    # Render inyecta DATABASE_URL
    DATABASE_URL = os.getenv("DATABASE_URL")

    # SQLAlchemy exige cambiar postgresql:// → postgresql+psycopg2://
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://")

    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False
