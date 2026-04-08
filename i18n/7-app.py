#!/usr/bin/env python3
"""
Flask app that mocks a login system, supports i18n (English/French),
and handles timezones.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration class for Flask-Babel"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user(login_as):
    """
    Returns a user dictionary or None if the ID cannot be found
    """
    if login_as is None:
        return None
    return users.get(login_as)


@app.before_request
def before_request():
    """Sets the global g.user for the request"""
    login_as = request.args.get("login_as", type=int)
    g.user = get_user(login_as)


def get_locale():
    """
    Determines the best language to use
    Priority:
    1. URL parameter 'locale'
    2. User's preferred locale
    3. Browser's Accept-Language
    4. Default locale
    """
    # 1. URL parameter
    locale_param = request.args.get("locale")
    if locale_param in app.config["LANGUAGES"]:
        return locale_param

    # 2. User's preferred locale
    if g.get("user") and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]

    # 3. Browser header
    browser_locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    if browser_locale:
        return browser_locale

    # 4. Default
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_timezone():
    """
    Determines the best timezone to use
    Priority:
    1. URL parameter 'timezone'
    2. User's timezone
    3. Default to UTC
    """
    # 1. URL parameter
    tz_param = request.args.get("timezone")
    if tz_param:
        try:
            return pytz.timezone(tz_param).zone
        except pytz.UnknownTimeZoneError:
            pass

    # 2. User's timezone
    if g.get("user") and g.user.get("timezone"):
        try:
            return pytz.timezone(g.user["timezone"]).zone
        except pytz.UnknownTimeZoneError:
            pass

    # 3. Default
    return app.config["BABEL_DEFAULT_TIMEZONE"]


# Initialize Babel with custom locale and timezone selectors
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def home():
    """Renders the home page template"""
    return render_template("7-index.html", timezone=get_timezone())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
