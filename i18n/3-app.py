#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel = Babel(app, locale_selector=get_locale)

@app.route("/")
def home():
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run(debug=True)