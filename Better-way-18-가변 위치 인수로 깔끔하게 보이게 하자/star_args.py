# -*- coding: utf-8 -*-
'''
## 핵심 정리

* def 문에서 *args를 사용하면 함수 가변 개수의 위치 인수를 받을 수 있다.
* * 연산자를 쓰면 시퀀스에 들어 있는 아이템을 함수의 위치 인수로 사용할 수 있다.
* 제너레이터와 * 연산자를 함께 사용하면 프로그램이 메모리 부족으로 망가질 수도 있다.
* *args를 받는 함수에서 새 위치 파라미터를 추가하면 정말 찾기 어려운 버그가 생길 수도 있다.
'''


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("%s: %s" % (message, values_str))

log("My numbers are", [1, 2])
log("Hi there", [])

'''
My numbers are: 1, 2
Hi there
'''


def log_sec(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("%s: %s" % (message, values_str))


log_sec("My nubmers are", 1, 2)
log_sec("Hi there")

'''
My nubmers are: 1, 2
Hi there
'''


favorites = [7, 33, 99]
log_sec("Favorite colors", *favorites)

'''
Favorite colors: 7, 33, 99
'''


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)

'''
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
'''


def log_third(sequence, message, *values):
    if not values:
        print("%s: %s" % (sequence, message))
    else:
        values_str = ", ".join(str(x) for x in values)
        print("%s: %s: %s" % (sequence, message, values_str))

log_third(1, "Favorites", 7, 33)
log_third("Favorite numbers", 7, 33)

'''
1: Favorites: 7, 33
Favorite numbers: 7: 33
'''
