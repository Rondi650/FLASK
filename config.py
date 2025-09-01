from sqlalchemy.engine import URL
from database import db

SECRET_KEY = 'Rondi'

def init_app(app):
    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Jogoteca;Trusted_Connection=yes;"
    connection_url = URL.create(
        "mssql+pyodbc", query={"odbc_connect": connection_string}
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
