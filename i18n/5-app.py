#!/usr/bin/env python3
"""
Flask app that mocks a login system and supports i18n (English/French)
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for Flask-Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """
    Retrieves a user from the 'login_as' URL parameter
    Returns:
        dict: user dictionary if found
        None: if login_as not present or invalid
    """
    try:
        user_id = int(request.args.get("login_as", ""))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """
    Executed before every request.
    Sets the global g.user for the request
    """
    g.user = get_user()


def get_locale():
    """
    Determines the best language to use
    Priority:
    1. 'locale' URL parameter if supported
    2. Logged-in user's locale if supported
    3. Browser's Accept-Language header
    """
    locale_param = request.args.get("locale")
    if locale_param in app.config["LANGUAGES"]:
        return locale_param

    if g.get("user") and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    """
    Renders the home page template
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
