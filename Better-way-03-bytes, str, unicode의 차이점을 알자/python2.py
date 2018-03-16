import os

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