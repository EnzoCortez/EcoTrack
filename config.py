import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-super-secreta")

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://localhost\\SQLEXPRESS/EcoTrackDB"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&trusted_connection=yes"
        "&Encrypt=no"
    )




    SQLALCHEMY_TRACK_MODIFICATIONS = False
