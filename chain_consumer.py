# coding=utf-8

import sys
import time
import logging

from celery import Celery
from kombu import Queue, Exchange
from celery.signals import setup_logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

BROKER_URL = "redis://127.0.0.1:6379/10"
BACKEND_URL = "redis://127.0.0.1:6379/11"

app = Celery("MyChain_Consumer", broker=BROKER_URL, backend=BACKEND_URL)

fn = lambda **kwargs: logging.getLogger()
setup_logging.connect(fn)


cloud_exchange = Exchange("MyChain", type="direct")

CELERY_QUEUES = (
    Queue("add", cloud_exchange, routing_key="add"),
    Queue("mul", cloud_exchange, routing_key="mul"),
    Queue("sub", cloud_exchange, routing_key="sub"),
    Queue("div", cloud_exchange, routing_key="div"),
)

CELERY_ROUTES = {
    "add": {"queue": "add", "routing_key": "add"},
    "mul": {"queue": "mul", "routing_key": "mul"},
    "sub": {"queue": "sub", "routing_key": "sub"},
    "div": {"queue": "div", "routing_key": "div"},
}


@app.task(name="add", routing_key="add")
def add(x, y):
    logging.debug("add x:{} + y:{}".format(x, y))
    time.sleep(1)
    return x + y


@app.task(name="mul", routing_key="mul")
def mul(x, y):
    logging.debug("mul x:{} + y:{}".format(x, y))
    time.sleep(1)
    return x * y


@app.task(name="sub", routing_key="sub")
def sub(x, y):
    logging.debug("sub x:{} + y:{}".format(x, y))
    time.sleep(1)
    return x - y


@app.task(name="div", routing_key="div")
def div(x, y):
    logging.debug("div x:{} + y:{}".format(x, y))
    time.sleep(1)
    return x / y
