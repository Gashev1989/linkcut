import random
from string import ascii_letters, digits

from flask import flash, redirect, render_template

from . import app, db
from .forms import URL_Form
from .models import URLMap


LETTERS_AND_DIGITS = ascii_letters + digits
MAX_CUSTOM_ID_LENGTH = 16
STRING_LENGTH = 6


def get_unique_short_id():
    random_string = ''.join(random.sample(LETTERS_AND_DIGITS, STRING_LENGTH))
    if URLMap.query.filter_by(short=random_string).first():
        random_string = get_unique_short_id()
    return random_string


def check_custom_id(custom_id):
    if len(custom_id) > MAX_CUSTOM_ID_LENGTH:
        return False
    for item in custom_id:
        if item not in LETTERS_AND_DIGITS:
            return False
    return True


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_Form()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('index.html', form=form)
        new_url = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(new_url)
        db.session.commit()
        return render_template(
            'index.html',
            form=form,
            url=new_url)
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)
