#!/bin/bash

FILE=".syncro"

if [ -f "$FILE" ];
then
  echo "Ya fue sincroniada"
else
  echo "Primer corrida"
  sleep 20 #esperando q levate bbdd
  python manage.py syncdb --noinput
  echo "from django.contrib.auth.models import User; User.objects.create_superuser('noresponder@libreqda.edu.uy', 'admin', 'admin')" | python manage.py shell
  touch ./$FILE
fi
python manage.py runserver 0.0.0.0:8000
