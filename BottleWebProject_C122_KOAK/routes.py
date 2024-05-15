"""
Routes and views for the bottle application.
"""

from re import template
from bottle import route, view, post, request, get
from datetime import datetime
import app

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/prima_algorithm_theory')
@view('prima_algorithm_theory')
def prima_theory():
    """Renders the Prima algorithm theory page."""
    return dict(
            title='Prima\'s algorithm theory',
            message='Prima\'s algorithm theory',
            year=datetime.now().year
        )

@route('/prima_algorithm_calc')
@view('prima_algorithm_calc')
def prima_theory():
    """Renders the Prima algorithm calculator page."""
    return dict(
            title='Prima\'s algorithm calculator',
            message='Prima\'s algorithm calculator',
            year=datetime.now().year
        )