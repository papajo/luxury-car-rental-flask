from flask import Flask, render_template, request
from flask_babel import Babel, _
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)

def get_locale():
    return request.accept_languages.best_match(['en', 'it']) or 'en'

babel = Babel(app, locale_selector=get_locale)

@app.route('/')
@app.route('/<lang>/')
def index(lang='en'):
    app.logger.debug(f"Rendering index page for lang={lang}")
    return render_template('index.html', lang=lang)

@app.route('/<lang>/services')
def services(lang):
    app.logger.debug(f"Rendering services page for lang={lang}")
    return render_template('services.html', lang=lang)

@app.route('/<lang>/services/<location>')
def service_location(lang, location):
    app.logger.debug(f"Rendering services page for lang={lang}, location={location}")
    return render_template('services.html', lang=lang, location=location)

@app.route('/<lang>/contact')
def contact(lang):
    app.logger.debug(f"Rendering contact page for lang={lang}")
    return render_template('contact.html', lang=lang)

@app.route('/<lang>/book')
def book(lang):
    app.logger.debug(f"Rendering book page for lang={lang}")
    return render_template('book.html', lang=lang)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')