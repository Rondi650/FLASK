from flask import Flask
from database import db
from config import SECRET_KEY, init_app
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = SECRET_KEY
init_app(app)
csrf = CSRFProtect(app)

with app.app_context():
    db.create_all()
    
from views import *

if __name__ == '__main__':
    app.run(debug=True)