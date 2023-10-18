FROM python:3.10.12-slim

RUN apt update && \
    apt install --no-install-recommends -y locales-all wait-for-it

RUN pip install --upgrade --no-cache-dir --upgrade pip

ADD requirements.txt /srv

RUN pip install --no-cache-dir -r /srv/requirements.txt

ADD alembic /srv/alembic/
ADD alembic.ini /srv/alembic.ini
ADD src /srv/src
WORKDIR /srv