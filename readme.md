Basic env setup:

python -m venv ~/env
source ~/env/bin/activate
deactivate

pip install -r requirements.txt


django-admin.py startproject profiles_project .
python manage.py startapp profiles_api

