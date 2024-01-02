from flask import Blueprint, render_template, request, redirect, url_for
from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@contacts.route("/new", methods=["POST"])
def add():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)
    
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('home'))

@contacts.route("/update")
def update():
    return render_template('about.html')

@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id) 
    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('home'))