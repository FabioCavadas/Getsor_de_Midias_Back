#!/bin/bash
set -e

until mysqladmin ping -h"$DB_HOST" --user="$DB_USER" --password="$DB_PASSWORD" --silent; do
  echo "Esperando o MySQL iniciar..."
  sleep 2
done

# Conecta ao MySQL e executa os comandos SQL
mysql -h"$DB_HOST" -u root -p"${DB_PASSWORD}" -e "CREATE USER IF NOT EXISTS 'us_gest_mid'@'%' IDENTIFIED BY '${DB_PASSWORD}';"
mysql -h"$DB_HOST" -u root -p"${DB_PASSWORD}" -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO 'us_gest_mid'@'%';"
mysql -h"$DB_HOST" -u root -p"${DB_PASSWORD}" -e "FLUSH PRIVILEGES;"

# Executa as migrações e inicia o servidor Django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
