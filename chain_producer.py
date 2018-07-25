# coding=utf-8

import sys
import logging

from celery import Celery
from celery import chain
from celery.signals import setup_logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

BROKER_URL = "redis://127.0.0.1:6379/10"
BACKEND_URL = "redis://127.0.0.1:6379/11"

app = Celery("MyChain_Producer", broker=BROKER_URL, backend=BACKEND_URL)
app.conf.update(
    CELERY_ROUTES={
        "add": {"queue": "add", "routing_key": "add"},
        "mul": {"queue": "mul", "routing_key": "mul"},
        "sub": {"queue": "sub", "routing_key": "sub"},
        "div": {"queue": "div", "routing_key": "div"},
    }
)

fn = lambda **kwargs: logging.getLogger()
setup_logging.connect(fn)


@app.task(name="add", routing_key="add")
def add(*args):
    pass


@app.task(name="mul", routing_key="mul")
def mul(*args):
    pass


@app.task(name="sub", routing_key="sub")
def sub(*args):
    pass


@app.task(name="div", routing_key="div")
def div(*args):
    pass


if __name__ == "__main__":

    logging.debug("**** producer run start ****")

    logging.debug('"同步"任务[等待执行结果]: 计算表达式(((2+2) + (3))*3)/3的值')
    res = chain(add.s(2, 2), add.s(3), mul.s(3), div.s(3))()
    res.get()
    logging.debug("result: {}".format(res.result))

    logging.debug('"异步"任务[不等待执行结果]: 计算表达式(((2+2) + (3))*3)/7的值')
    chain(add.s(2, 2), add.s(3), mul.s(3), div.s(7))()

    logging.debug("**** producer run end ****")
