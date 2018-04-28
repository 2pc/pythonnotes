#! /usr/bin/env python
from celery.task import task

# 自定义要执行的task任务
@task
def print_hello():
    return 'hello celery and django...'
@task
def print_hello2():
    return 'hello2 celery and django...'
