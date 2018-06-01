#!/usr/bin/env bash

VERSION=1.0

INSTANCE_HOME=/srv/aviasales_hakaton
APP_SRC=${INSTANCE_HOME}/aviasales_hakaton
DJANGO_SETTINGS_MODULE=aviasales_hakaton.settings

docker run \
	--rm \
	-ti \
	--name aviasales_hakaton \
	-e DBHOST=dbhost \
	-e DBNAME=dbname \
	-e DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE} \
	-v static:${APP_SRC}/static \
	-v media:${APP_SRC}/media \
	-p 8080:8080 \
	aviasales_hakaton:${VERSION}
