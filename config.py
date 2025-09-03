from sqlalchemy.engine import URL
from database import db
from pathlib import Path

SECRET_KEY = 'Rondi'

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_PATH = BASE_DIR / 'uploads'

def init_app(app):
    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Jogoteca;Trusted_Connection=yes;"
    connection_url = URL.create(
        "mssql+pyodbc", query={"odbc_connect": connection_string}
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_PATH'] = str(UPLOAD_PATH)
    db.init_app(app)
