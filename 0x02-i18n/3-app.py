#!/usr/bin/env python3
'''Parametrize templates'''


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''class configuration for babel'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    '''get the best match language'''
    return request.accept_languages.best_match(Config.LANGUAGES)


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def hello_world():
    '''rendering hello world page'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
