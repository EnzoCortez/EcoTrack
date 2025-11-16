import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-super-secreta")

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@ENZO\\SQLEXPRESS/EkoTrackDB"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Trusted_Connection=yes"
        "&Encrypt=no"
)




    SQLALCHEMY_TRACK_MODIFICATIONS = False
