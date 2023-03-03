"""
Routes and views for the flask application.
"""
from Capstone.models import db
from datetime import datetime
from flask import render_template
from Capstone import app

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', title = '500 Forbidden', year=datetime.now().year,
                               ), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title = '404 Not Found', year=datetime.now().year,
                               ), 404

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# web resource page - lily
@app.route('/resources')
def resources():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )