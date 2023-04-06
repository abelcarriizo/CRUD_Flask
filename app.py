from flask import Flask
from routes.contacts import contacts

app = Flask(__name__)

#Settings   
app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://abel:123@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.register_blueprint(contacts)