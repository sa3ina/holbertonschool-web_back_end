#!/usr/bin/env python3
"""
Flask app with mocked user login and i18n (Flask-Babel 2.x+)
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    try:
        user_id = int(request.args.get("login_as", ""))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    g.user = get_user()


# Use locale_selector instead of @babel.localeselector
def get_locale():
    locale_param = request.args.get("locale")
    if locale_param in app.config["LANGUAGES"]:
        return locale_param

    if g.get("user") and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)