# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 키워드 인수는 함수 호출의 의도를 더 명확하게 해준다.
* 특히 불 플래그를 여러 개 받는 함수처럼 헷갈리기 쉬운 함수를 호출할 때 키워드 인수를 넘기게 하려면 키워드 전용 인수를 사용하자.
* 파이썬 3는 함수의 키워드 전용 인수 문법을 명시적으로 지원한다.
* 파이썬 2에서는 **kwargs를 사용하고 TypeError 예외를 직접 일으키는 방법으로 함수의 키워드 전용 인수를 흉내 낼 수 있다.
'''


def safe_division(number, divisor, ignore_overflow,
    ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise

result = safe_division(1, 10**500, True, False)
print(result)

result = safe_division(1, 0, False, True)
print(result)

'''
0
inf
'''



def safe_division_b(number, divisor,
    ignore_overflow=False,
    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise

result = safe_division_b(1, 10*500, ignore_overflow=True)
print(result)

result = safe_division_b(1, 0, ignore_zero_division=True)
print(result)

# still works
result = safe_division_b(1, 10**500, True, False)
print(result)


'''
0
inf
0
'''


def print_args(*args, **kwargs):
    print "Positional:  ", args
    print "Keyword:     ", kwargs

print_args(1, 2, foo="bar", stuff="meep")

'''
Positional:   (1, 2)
Keyword:      {'foo': 'bar', 'stuff': 'meep'}
'''


def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop("ignore_overflow", False)
    ignore_zero_division = kwargs.pop("ignore_zero_division", False)

    if kwargs:
        raise TypeError("Unexpected **kwargs: %r" % kwargs)
    
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise

safe_division_d(1, 10)
safe_division_d(1, 0, ignore_zero_division=True)
safe_division_d(1, 10**500, ignore_overflow=True)

# not works
# safe_division_d(1, 0, False, True)

# not works
# safe_division_d(0, 0, unexpected=True)