"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@view('index')
def home():
    """Renders the home page."""
    return dict(
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

@route('/daykstar_algorithm_theory')
@view('daykstar_algorithm_theory')
def daykstar_theory():
    """Renders the Daykstar algorithm theory page."""
    return dict(
            title='Daykstar\'s algorithm theory',
            message='Daykstar\'s algorithm theory',
            year=datetime.now().year
        )

@route('/floyd_algorithm_theory')
@view('floyd_algorithm_theory')
def floyd_theory():
    """Renders the Floyd algorithm theory page."""
    return dict(
            title='Floyd\'s algorithm theory',
            message='Floyd\'s algorithm theory',
            year=datetime.now().year
        )

@route('/kraskal_algorithm_theory')
@view('kraskal_algorithm_theory')
def kraskal_theory():
    """Renders the Kraskal algorithm theory page."""
    return dict(
            title='Kraskal\'s algorithm theory',
            message='Kraskal\'s algorithm theory',
            year=datetime.now().year
        )

@route('/prima_algorithm_calc')
@view('prima_algorithm_calc')
def prima_calc():
    """Renders the Prima algorithm calculator page."""
    return dict(
            title='Prima\'s algorithm calculator',
            message='Prima\'s algorithm calculator',
            year=datetime.now().year
        )

@route('/daykstar_algorithm_calc')
@view('daykstar_algorithm_calc')
def daykstar_calc():
    """Renders the Daykstar algorithm calculator page."""
    return dict(
            title='Daykstar\'s algorithm calculator',
            message='Daykstar\'s algorithm calculator',
            year=datetime.now().year
        )

@route('/floyd_algorithm_calc')
@view('floyd_algorithm_calc')
def floyd_calc():
    """Renders the Floyd algorithm calculator page."""
    return dict(
            title='Floyd\'s algorithm calculator',
            message='Floyd\'s algorithm calculator',
            year=datetime.now().year
        )

@route('/kraskal_algorithm_calc')
@view('kraskal_algorithm_calc')
def kraskal_calc():
    """Renders the Kraskal algorithm calculator page."""
    return dict(
            title='Kraskal\'s algorithm calculator',
            message='Kraskal\'s algorithm calculator',
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