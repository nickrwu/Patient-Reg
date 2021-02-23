release: sh -c 'cd ./backend/src/ && python manage.py migrate'
web: sh -c 'cd ./backend/src/ && exec gunicorn backend.wsgi --log-file -'