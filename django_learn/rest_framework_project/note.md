1 setting.py add

INSTALLED_APPS = (
    'rest_framework',)

2. app add serializers.py

3. views.py set

4. urls.py set


--------------------------------

python manage.py createsuperuser --username vitor --email vitor@example.com
python manage.py drf_create_token vitor

curl http://127.0.0.1:8000/hello/ -H 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'


curl -X POST http://127.0.0.1:8000/api-token-auth/ -d "username=vitor&password=123456"
