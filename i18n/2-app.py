#!/usr/bin/env python3
"""
Flask-Babel
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)


def get_locale():
    """Determines the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(locale_selector=get_locale)
babel.init_app(app)


@app.route("/")
def home():
    """Route that returns a template"""
    return render_template('2-index.html')
