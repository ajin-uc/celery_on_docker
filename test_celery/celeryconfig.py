broker_url = 'amqp://172.17.0.2:5672//'

result_backend = 'db+postgresql://postgres:postgres@172.17.0.4:5432/celery_test_base'

imports = ('test_celery.tasks', )
