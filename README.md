Celery Chain Demo
===

Linux平台下以守护进程方式运行Celery任务Demo<br/>

Environment
==========
Python 3.5<br/>
Celery 4.2.1<br/>

Usage
====
1. 激活虚拟环境<br/>
`pipenv shell`

2. 启动celery<br/>
`celery -A chain_consumer.app worker -l debug --config=chain_consumer`

3. 执行脚本chain_producer.py，添加任务<br/>
`python chain_producer.py`

Installation
============
1. `git clone https://github.com/Wayde2014/celery-chain-demo`<br/>
2. `pipenv install`<br/>