## Проект api_final_yatube

Проект для практической отработки возможностей API. Доступен функционал по добавлению материалов, редактированию, удалению, комментированию, подписки на авторов, отписки и т.д.

## Технологии

Python 3.9, Django 3.2, Django Rest Framework

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:rest2011/api_final_yatube.git
cd yatube_api

Cоздать и активировать виртуальное окружение:

python -m venv venv
source venv/Source/activate

Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:

python manage.py migrate

Запустить проект:

python manage.py runserver

## Автор 
Хаматьяров Ринат github.com/rest2011
