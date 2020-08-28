command = '/home/pi/code/TODO-manager/env/bin/gunicorn'
pythonpath = '/home/pi/code/TODO-manager/src'
bind = '127.0.0.1:8001'
workers = 9
user = 'pi'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=configs.settings'
