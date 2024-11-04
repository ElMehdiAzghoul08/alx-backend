#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Any, Union, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """Get user"""
    login_id = request.args.get('login_as')
    if login_id and login_id.isdigit():
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Before request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Select language"""
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


_ = _ if _ else lambda x: x


@app.route('/', strict_slashes=False)
def index() -> str:
    """Home page"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
