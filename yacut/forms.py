from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


MIN_LINK_LENGTH = 1
MAX_ORIGINAL_LINK_LENGTH = 256
MAX_SHORT_LINK_LENGTH = 16


class URL_Form(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_LINK_LENGTH, MAX_ORIGINAL_LINK_LENGTH)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(MIN_LINK_LENGTH, MAX_SHORT_LINK_LENGTH),
                    Optional()]
    )
    submit = SubmitField('Создать')
