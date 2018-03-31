# -*- coding: utf-8 -*-
from datetime import datetime
from time import sleep

import json

'''
## 핵심 정리

* 기본 인수는 모듈 로드 시점에 함수 정의 과정에서 딱 한 번만 평가된다. 그래서 ({}나 []와 같은) 동적 값에는 이상하게 동작하는 원인이 되기도 한다.
* 값이 동적인 키워드 인수에는 기본값으로 None을 사용하자. 그러고 나서 함수의 docstring에 실제 기본 동작을 문서화하자.
'''


def log(message, when=datetime.now()):
    print("%s: %s" % (when, message))

log("Hi there!")
sleep(0.1)
log("Hi again!")

'''
2018-03-31 12:25:20.622215: Hi there!
2018-03-31 12:25:20.622215: Hi again!
'''


def log_time(message, when=None):
    """Log a message with a timestamp
    
    Arguments:
        message {str} -- Message to print.
    
    Keyword Arguments:
        when {datetime.datetime} -- tatetime of when the message occurred.
            Defaults to the present time. (default: {None})
    """

    when = datetime.now() if when is None else when
    print("%s: %s" % (when, message))

log_time("Hi there!")
sleep(0.1)
log_time("Hi again!")

'''
2018-03-31 12:29:04.592860: Hi there!
2018-03-31 12:29:04.693837: Hi again!
'''


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode("bad data")
foo["stuff"] = 5

bar = decode("also bad")
bar["meep"] = 1

assert foo is bar

print("Foo: ", foo)
print("Bar: ", bar)


'''
Foo:  {'meep': 1, 'stuff': 5}
Bar:  {'meep': 1, 'stuff': 5}
'''


def decode_default(data, default=None):
    """Load JSON data from a string
    
    Arguments:
        data {str} -- JSON data to decode.
    
    Keyword Arguments:
        default {dic} -- Value to return if decoding fails.
            Defaults to an empty dictionary (default: {None})
    """

    if default is None:
        default = {}
    
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode_default("bad data")
foo["stuff"] = 5

bar = decode_default("also bad")
bar["meep"] = 1

print("Foo: ", foo)
print("Bar: ", bar)


'''
Foo:  {'stuff': 5}
Bar:  {'meep': 1}
'''
