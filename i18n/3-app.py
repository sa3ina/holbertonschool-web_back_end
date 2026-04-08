#!/usr/bin/env python3
"""
Basic Flask app with Babel internationalization
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Configuration class for Babel settings
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """
    Select the best matching language from the request
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    """
    Render the home page
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
