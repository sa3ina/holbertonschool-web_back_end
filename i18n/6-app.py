#!/usr/bin/env python3
"""
This module is for Babel object instantiation
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel


class Config:
    """
    This class is for configuring the languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """
    Determines the best language to use in this order:
    1. URL parameter 'locale'
    2. User's preferred locale
    3. Browser's Accept-Language
    4. Default locale
    """
    # 1. Check URL parameter
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param

    # 2. Check logged-in user's locale
    if g.get('user') and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Check browser header
    browser_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if browser_locale:
        return browser_locale

    # 4. Default
    return app.config['BABEL_DEFAULT_LOCALE']
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
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
