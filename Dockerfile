FROM python:2.7
MAINTAINER Lu Pa <admin@tedic.org>

ENV DEBIAN_FRONTEND noninteractive
ENV CODE /usr/src/libreqda

RUN apt-get update \
	&& apt-get -y dist-upgrade

RUN apt-get install -y libmysqlclient-dev \
	libevent-dev \
	libxml2-dev \
	libxslt1-dev

#Creo dos carpetas libreqda una dentro de la otra
RUN mkdir -p $CODE/libreqda

COPY manage.py $CODE
COPY requirements.txt $CODE 
COPY libreqda $CODE/libreqda
COPY local_settings.py $CODE/libreqda

WORKDIR $CODE

RUN pip install -r requirements.txt


