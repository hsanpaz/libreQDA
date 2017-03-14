#!/bin/bash

FILE=".syncro"

if [ -f "$FILE" ];
then
   echo "Ya fue sincroniada"
else
  echo "Primer corrida"
  sleep 10 #esperando q levate bbdd
  touch ./$FILE
  python manage.py syncdb
fi
python manage.py runserver 0.0.0.0:8000
