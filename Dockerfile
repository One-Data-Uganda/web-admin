# syntax = docker/dockerfile:experimental
FROM python:3.8-slim

LABEL com.centurylinklabs.watchtower.enable="true"

WORKDIR /project

ADD static /project/static

ADD requirements.txt /project

RUN --mount=type=cache,target=/root/.cache/pip pip3.8 install -r /project/requirements.txt

ADD config.py requirements.txt celeryconfig.py wsgi.py /project/

ADD app /project/app

ENTRYPOINT [ "gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "wsgi:asgi_app", "--bind", "0.0.0.0:5000" ]
