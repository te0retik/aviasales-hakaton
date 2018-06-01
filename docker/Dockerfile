FROM ubuntu:16.04

ENV INSTANCE_HOME=/srv/aviasales_hakaton \
	APP_SRC=/srv/aviasales_hakaton/aviasales_hakaton \
	DJANGO_SETTINGS_MODULE=aviasales_hakaton.settings

RUN export DEBIAN_FRONTEND=noninteractive \
	&& apt-get update -y && apt-get upgrade -y \
	&& apt-get install -y nginx-light python3 python3-pip python3-psycopg2 \
	&& BUILD_DEPS='build-essential python3-dev' \
	&& apt-get install -y ${BUILD_DEPS} \
	&& pip3 install --no-cache-dir circus==0.13.0 gunicorn==19.5.0 \
	&& apt-get autoremove -y ${BUILD_DEPS} \
	&& apt-get clean && rm -rf /tmp/* /var/tmp/* \
	&& mkdir ${INSTANCE_HOME}

WORKDIR ${INSTANCE_HOME}
COPY ./aviasales_hakaton ${APP_SRC}
RUN pip3 install --no-cache-dir -r ${APP_SRC}/requirements.txt \
	&& pip3 install PyZMQ\<17.0 tornado\<5.0

COPY ./docker/circus-web.ini /etc/circus/web.ini
COPY ./docker/nginx-default-site.conf /etc/nginx/sites-available/default
COPY ./docker/gunicorn.py .
RUN chown -R www-data ${INSTANCE_HOME} \
	/etc/circus/web.ini \
	/etc/nginx/sites-available/default

WORKDIR ${APP_SRC}

RUN nginx -T \
	&& python3 -c 'import os, compileall; compileall.compile_dir(os.curdir, force=1)' \
	&& python3 manage.py collectstatic --no-input

RUN apt-get install -y net-tools

#USER www-data

CMD ["circusd", "/etc/circus/web.ini"]
