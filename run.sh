#!/bin/bash

FILE=".syncro"

if [ -f "$FILE" ];
then
  echo "Ya fue sincroniada"
else
  echo "Primer corrida"
  sleep 20 #esperando q levate bbdd
  echo "Sincronizando"
  python manage.py syncdb --noinput &&  touch ./$FILE
fi
echo "Levantando el server"
python manage.py runserver 0.0.0.0:8000
