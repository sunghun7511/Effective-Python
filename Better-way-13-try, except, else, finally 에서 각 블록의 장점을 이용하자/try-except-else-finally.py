# -*- coding: utf-8 -*-w
import json

'''
## 핵심 정리 

* try/finally 복합문을 이용하면 try 블록에서 예외 발생 여부와 상관없이 정리 코드를 실행할 수 있다.
* else 블록은 try 블록에 있는 코드의 양을 최소로 줄이는 데 도움을 주며 try/except 블록과 성공한 경우에 실행할 코드를 시각적으로 구분해준다.
* else 블록은 try 블록의 코드가 성공적으로 실행된 후 finally 블록에서 공통 정리 코드를 실행하기 전에 추가 작업을 하는 데 사용할 수 있다.
'''


handle = open("./random_data.txt")
# IOError가 일어날 수 있음.

try:
    data = handle.read()
    # UnicodeDecodeError 가 일어날 수 있음.
finally:
    handle.close()


def load_json_key(data, key):
    try:
        result_dict = json.loads(data)
        # ValueError 가 일어날 수 있음
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]
        # KeyError 가 일어날 수 있음


UNDEFINED = object()

def divide_json(path):
    handle = open("path", "r+")
    # IOError 가 일어날 수 있음
    try:
        data = handle.read()
        # UnicodeDecodeError 가 일어날 수 있음
        op = json.loads(data)
        # ValueError 가 일어날 수 있음
        value = (
            op["numerator"] /
            op["denominator"]
            # ZeroDivisionError 가 일어날 수 있음
        )
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op["result"] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        # IOError 가 일어날 수 있음
        return value
    finally:
        handle.close()
        # 항상 실행함