# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 클로저 함수는 자신이 정의된 스코프 중 어디에 있는 변수도 참조할 수 있다.
* 기본적으로 클로저에서 변수를 할당하면 바깥쪽 스코프에는 영향을 미치지 않는다.
* 파이썬 3에서는 nonlocal 문을 사용하여 클로저를 감싸고 있는 스코프의 변수를 수정할 수 있음을 알린다.
* 파이썬 2에서는 (아이템이 한 개만 있는 리스트 같은) 수정 가능한 값으로 nonlocal 문이 없는 문제를 우회한다.
* 간단한 함수 이외에는 nonlocal 문을 사용하지 말자.
'''


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

'''
[2, 3, 5, 7, 1, 4, 6, 8]
'''


def sort_priority2(numbers, group):
    found = False           # 스코프: 'sort_priority2'

    def helper(x):
        if x in group:
            found = True    # 스코프: 'helper'
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)

print("Found : ", found)
print(numbers)

'''
Found :  False
[2, 3, 5, 7, 1, 4, 6, 8]
'''


def sort_priority3(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority3(numbers, group)

print("Found : ", found)
print(numbers)

'''
Found :  True
[2, 3, 5, 7, 1, 4, 6, 8]
'''


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False
    
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)
    

sorter = Sorter(group)
numbers.sort(key=sorter)

assert sorter.found is True

print("Found : ", sorter.found)
print(numbers)

'''
Found :  True
[2, 3, 5, 7, 1, 4, 6, 8]
'''

'''
In python2


def sort_priority(numbers, group):
    found = [False]

    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found[0]
'''