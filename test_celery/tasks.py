from __future__ import absolute_import, unicode_literals
from test_celery.celery import app

@app.task
def reverser(string):
    return string[::-1]
