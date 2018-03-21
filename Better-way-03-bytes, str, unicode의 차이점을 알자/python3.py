# -*- coding: utf-8 -*-
import os

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value


'''
파이썬 3에서는 bytes와 str 인스턴스는 빈 문자열이더라도 절대 같지 않다.
파이썬 2의 str 과 unicode처럼 동시에 사용할 수 없다.

파이썬 2에서는 동작하지 않는 다음 코드는, 바이트 출력이 아니라 그렇다.

with open("/tmp/random.bin", "w") as f:
    f.write(os.urandom(10))

해결은 "wb" 를 통해  바이트라는 것을 알려주면 된다.

'''

with open("/tmp/random.bin", "wb") as f:
    f.write(os.urandom(10))