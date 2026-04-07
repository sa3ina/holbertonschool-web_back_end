#!/usr/bin/env python3
"""
Babel object instantiation
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel


class Config:
    """
    Configuring the languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """
    Determines the best match for supported languages
    """
    if request.args.get('locale'):
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """
    Returns a user dictionary or None if the ID cannot be found
    """
    if login_as is None:
        return None
    if login_as not in users:
        return None
    return users.get(login_as)


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """
    Finds a user if any, and sets it as a global on flask.g.user
    """
    login_as = request.args.get('login_as', type=int)
    g.user = get_user(login_as)


@app.route('/')
def home():
    """
    Renders the template
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
