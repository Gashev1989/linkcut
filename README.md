# Проект LinkCut
### Описание
Проект LinkCut — это сервис укорачивания ссылок.
***
Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.
***
Пользовательский интерфейс сервиса — одна страница с формой.
Эта форма состоит из двух полей:
- обязательного - для длинной исходной ссылки;
- необязательного - для пользовательского варианта короткой ссылки.
***
API проекта доступен всем желающим. 
Сервис обслуживает два эндпоинта:
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному идентификатору короткой ссылки.

### Технологии
**Язык:**  
Python 3.9  
**Библиотеки:**  
Flask  
SQLAlchemy  

### Запуск проекта локально
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Gashev1989/yacut.git
```
```
cd yacut
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
3. Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
4. В корневой директории проекта создать файл .env, в котором указать:
```
FLASK_APP=yacut
FLASK_ENV=development (или production)
DATABASE_URI='sqlite:///db.sqlite3' (или иную БД)
SECRET_KEY='SECRET_KEY' (придумайте свой ключ)
```
5. Создать базу данных для чего выполнить команды поочередно:
```
(venv) ... $ flask shell
>>> from opinions_app import db
>>> db.create_all()
>>> exit()
```
*Метод* create_all() *создаёт базу данных, если её ещё нет в проекте, а если база есть, то создаются таблицы в ней*

6. Из корневой директории запустить приложение командой:
```
flask run
```

### Примеры запросов API
1. Запрос на создание новой короткой ссылки
[POST] /api/id/
```
{
  "url": "https://www.python.org/success-stories/category/software-development/",
  "custom_id": "Development"
}
```
*Если поле "custom_id" не заполнить, то API сгенерирует рандомную ссылку.*

Response
```
{
  "short_link": "http://127.0.0.1:5000/Development",
  "url": "https://www.python.org/success-stories/category/software-development/"
}
```
2. Запрос на получение оригинальной ссылки по указанному короткому идентификатору короткой ссылки
[GET] /api/id/Development

Response
```
{
  "url": "https://www.python.org/success-stories/category/software-development/"
}
```

### Автор
Гашев Константин