from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new')
def add():
    return 'saving contact'

@contacts.route('/update')
def update():
    return 'update a contact'

@contacts.route('/delete')
def delete():
    return 'delete a contact'