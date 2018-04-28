#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
create by zuzeep at 16/08/2017
'''

from __future__ import absolute_import, unicode_literals
import os

import datetime
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproj.settings')

app = Celery('celeryproj')
app.now = datetime.datetime.utcnow

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
