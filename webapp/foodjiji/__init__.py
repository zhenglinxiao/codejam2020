from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:onion@localhost/foodjiji'
db = SQLAlchemy(app)

from foodjiji import routes