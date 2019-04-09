# NSU Social
conda create --name myDjangoEnv django


activate myDjangoEnv


django-admin startproject myproject
cd myproject

py manage.py startapp myapp

py manage.py startapp first_app

py manage.py makemigrations
py manage.py migrate


Package install:
conda install -c conda-forge django-crispy-forms

conda install -c anaconda pillow 

pip install django-braces

pip install pyinstaller
pyinstaller -w -F -i "D:\Python\Compiler_Test\icon.ico" compiler.py


Admin page:
py manage.py makemigraions
py manage.py migrate
py manage.py createsuperuser
