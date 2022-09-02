#!/bin/bash

cd backend

echo "Instalando dependências"
pip install -r requirements.txt

echo "Realizando migrações..."
py manage.py makemigrations
py manage.py migrate

echo "-----------------------------------------"
echo "Projeto sendo inicializado com sucesso..."
echo "-----------------------------------------"
py manage.py runserver
