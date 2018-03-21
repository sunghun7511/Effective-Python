# -*- coding: utf-8 -*-
import os

'''
## 핵심 정리

* 파이썬 3에서 bytes는 8비트 값을 저장하고, str은 유니코드 문자를 저장한다. >나 +와 같은 연산자에 bytes와 str 인스턴스를 함께 사용할 수 없다.
* 파이썬 2에서 str은 8비트 값을 저장하고, unicode는 유니코드 문자를 저장한다. str이 7비트 아스키 문자만 포함한다면 연산자에 str과 unicode를 함께 사용할 수 있다.
* 헬퍼 함수를 사용해서 처리할 입력값이 원하는 문자 시퀀스 타입(8비트 값, UTF-8 인코딩 문자, 유니코드 문자 등)으로 되어 있게 한다.
* 바이너리 데이터를 파일에서 읽거나 쓸 때는 파일을 바이너리 모드("rb" 혹은 "wb")로 오픈한다.
'''


def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode("utf-8")
    else:
        value = unicode_or_str
    return value


def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode("utf-8")
    else:
        value = unicode_or_str
    return value


'''
파이썬 2에서는 str이 7비트 아스키 문자만 포함하고 있다면, unicode와 str 인스턴스가 같은 타입처럼 보인다.

예를 들어 7비트 아스키만 처리하는 경우 str 또는 unicode를 받는 함수에
str이나 unicode 인스턴스를 넘겨도 문제 없이 동작한다.

실제 예로 아래 코드는 파이썬 2에서는 동작하지만, 3에서는 동작하지 않는다.
'''

with open("/tmp/random.bin", "w") as f:
    f.write(os.urandom(10))