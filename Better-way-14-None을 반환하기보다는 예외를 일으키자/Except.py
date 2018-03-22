# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 특별한 의미를 나타내려고 None을 반환하는 함수가 오류를 일으키기 쉬운 이유는 None이나 다른 값(예를 들면 0이나 빈 문자열)이 조건식에서 False로 평가되기 때문이다.
* 특별한 상황을 알릴 때 None을 반환하는 대신에 예외를 일으키자. 문서화가 되어 있다면 호출하는 코드에서 예외를 적절하게 처리할 것이라고 기대할 수 있다.
'''


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 8, 0

result = divide(x, y)
if result is None:
    print("Invalid inputs")

'''
Invalid inputs
'''


x, y, = 0, 5
result = divide(x, y)
if not result:
    print("Invalid inputs")
    # 잘못되었다.

'''
Invalid inputs
'''


def safe_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


success, result = safe_divide(x, y)

if not success:
    print("Invalid inputs")
else:
    print("Result is %d" % result)

'''
Result is 0
'''


_, result = safe_divide(x, y)

if not result:
    print("Invalid inputs")

'''
Invalid inputs
'''


def raise_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e


x, y = 5, 2

try:
    result = divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print("Result is %.1f" % result)

'''
Result is 2.5
'''