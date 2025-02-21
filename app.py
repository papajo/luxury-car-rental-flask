from flask import Flask, render_template, request, flash, redirect, url_for
from flask_babel import Babel, _
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Email
import logging, os

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()  # Replace with a secure random string (e.g., os.urandom(24).hex())
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)

def get_locale():
    lang = request.view_args.get('lang', request.accept_languages.best_match(['en', 'it']))
    return lang if lang in ['en', 'it'] else 'en'

babel = Babel(app, locale_selector=get_locale)

# Forms
class ContactForm(FlaskForm):
    name = StringField(_('Name'), validators=[DataRequired()])
    email = EmailField(_('Email'), validators=[DataRequired(), Email()])
    message = TextAreaField(_('Message'), validators=[DataRequired()])
    submit = SubmitField(_('Send'))

class BookingForm(FlaskForm):
    service = SelectField(_('Service'), choices=[
        ('rolls-royce', _('Rolls-Royce Phantom')),
        ('wedding', _('Wedding Car')),
        ('party', _('Private Party Car'))
    ], validators=[DataRequired()])
    location = SelectField(_('Location'), choices=[
        ('naples', _('Naples')),
        ('salerno', _('Salerno')),
        ('avellino', _('Avellino')),
        ('benevento', _('Benevento')),
        ('montoro', _('Montoro')),
        ('montesarchio', _('Montesarchio')),
        ('sangiorgiodelsannio', _('San Giorgio del Sannio')),
        ('caserta', _('Caserta')),
        ('aversa', _('Aversa')),
        ('marcianise', _('Marcianise')),
        ('cavadetirrenti', _('Cava de’ Tirreni')),
        ('battipaglia', _('Battipaglia')),
        ('giuglianoincampania', _('Giugliano in Campania')),
        ('torredelgreco', _('Torre del Greco'))
    ], validators=[DataRequired()])
    date = DateField(_('Date'), validators=[DataRequired()])
    email = EmailField(_('Email'), validators=[DataRequired(), Email()])  # Add email field
    submit = SubmitField(_('Book Now'))

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

@app.route('/<lang>/contact', methods=['GET', 'POST'])
def contact(lang):
    app.logger.debug(f"Rendering contact page for lang={lang}")
    form = ContactForm()
    if form.validate_on_submit():
        app.logger.debug(f"Contact form submitted: {form.name.data}, {form.email.data}, {form.message.data}")
        flash(_('Your message has been sent!'), 'success')
        return redirect(url_for('contact', lang=lang))
    return render_template('contact.html', lang=lang, form=form)

@app.route('/<lang>/book', methods=['GET', 'POST'])
def book(lang):
    app.logger.debug(f"Rendering book page for lang={lang}")
    form = BookingForm()
    if form.validate_on_submit():
        app.logger.debug(f"Booking form submitted: {form.service.data}, {form.location.data}, {form.date.data}, {form.email.data}")
        flash(_('Your booking has been submitted!'), 'success')
        return redirect(url_for('book', lang=lang))
    return render_template('book.html', lang=lang, form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')