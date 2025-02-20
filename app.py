from flask import Flask, render_template, request, send_from_directory 
import os
from flask_babel import Babel, _

app = Flask(__name__)

def get_locale():
    return request.accept_languages.best_match(['en', 'it']) or 'en'

babel = Babel(app, locale_selector=get_locale)

@app.route('/') 
def home(): return render_template('index.html')

@app.route('/static/') 
def serve_static(filename): 
    root_dir = os.path.dirname(os.getcwd()) 
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

def create_app(): return app 

@app.route('/')
@app.route('/<lang>/')
def index(lang='en'):
    return render_template('index.html', lang=lang)

@app.route('/<lang>/services')
def services(lang):
    return render_template('services.html', lang=lang)

@app.route('/<lang>/contact')
def contact(lang):
    return render_template('contact.html', lang=lang)

@app.route('/<lang>/book')
def book(lang):
    return render_template('book.html', lang=lang)

if __name__ == '__main__':
    app.run(debug=True)