from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import check_custom_id, get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or data['custom_id'] in ('', None):
        data['custom_id'] = get_unique_short_id()
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    elif not check_custom_id(data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    new_link = URLMap()
    new_link.from_dict(data)
    db.session.add(new_link)
    db.session.commit()
    return jsonify(new_link.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def redirect_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(url=url.original), 200
