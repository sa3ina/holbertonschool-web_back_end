#!/usr/bin/env python3
"""
Flask app with URL-forced locale support
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Configuration for supported languages and default locale
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """
    Determines the best matching language.

    - If 'locale' URL parameter exists and is supported, use it
    - Otherwise, fallback to browser's accepted languages
    """
    locale_param = request.args.get("locale")
    if locale_param in app.config["LANGUAGES"]:
        return locale_param
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    """Render the home page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)