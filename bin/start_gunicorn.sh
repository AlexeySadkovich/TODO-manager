#!/bin/bash
source /home/pi/code/TODO-manager/env/bin/activate
exec gunicorn -c "/home/pi/code/TODO-manager/src/gunicorn_config.py" configs.wsgi
