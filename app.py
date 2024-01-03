from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  env_config import DATABASE_CONNECTION_URI
from routes.contacts import contacts

app = Flask(__name__)

app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAlchemy(app)

app.register_blueprint(contacts)
