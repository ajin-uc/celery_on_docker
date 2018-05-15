FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt


COPY . /code/
WORKDIR /code/

EXPOSE 80

ENTRYPOINT celery -A test_celery worker -l info
