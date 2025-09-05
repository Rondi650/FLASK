from sqlalchemy.engine import URL
from database import db
import os

SECRET_KEY = 'Rondi'

UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'uploads')
os.makedirs(UPLOAD_PATH, exist_ok=True)

def init_app(app):
    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Jogoteca;Trusted_Connection=yes;"
    connection_url = URL.create(
        "mssql+pyodbc", query={"odbc_connect": connection_string}
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_PATH'] = UPLOAD_PATH
    db.init_app(app)