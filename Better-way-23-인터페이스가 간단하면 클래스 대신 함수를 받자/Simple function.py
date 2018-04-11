# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 파이썬에서 컴포넌트 사이의 간단한 인터페이스용으로 클래스를 정의ㅣ하고 인스턴스를 생성하는 대신에 함수만 써도 종종 충분하다.
* 파이썬에서 함수와 메서드에 대한 참조는 일급이다. 즉, 다른 타입처럼 표현식에서 사용할 수 있다.
* __call__ 이라는 특별한 메서드는 클래스의 인스턴스를 일반 파이썬 함수처럼 호출할 수 있게 해준다.
* 상태를 보존하는 함수가 필요할 때 상태 보존 클로저를 정의하는 대신 __call__ 메서드를 제공하는 클래스를 정의하는 방안을 고려하자.
'''

from collections import defaultdict

names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
names.sort(key=lambda x: len(x))
print(names)

'''
['Plato', 'Socrates', 'Aristotle', 'Archimedes']
'''


def log_missing():
    print("Key added")
    return 0

current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]
result = defaultdict(log_missing, current)
print("Before: ", dict(result))
for key, amount in increments:
    result[key] += amount
print("After: ", dict(result))

'''
Before:  {'green': 12, 'blue': 3}
Key added
Key added
After:  {'red': 5, 'green': 12, 'blue': 20, 'orange': 9}
'''


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # 상태 보존 클로저
        added_count += 1
        return 0
    
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


result, count = increment_with_report(current, increments)

print(dict(result))
print(count)

'''
{'orange': 9, 'red': 5, 'green': 12, 'blue': 20}
2
'''


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current) # 메서드 참조

for key, amount in increments:
    result[key] += amount

print(dict(result))
print(counter.added)

'''
{'red': 5, 'green': 12, 'blue': 20, 'orange': 9}
2
'''


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0
    
    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()

print(callable(counter))

'''
True
'''


counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount

print(dict(result))
print(counter.added)

'''
{'green': 12, 'blue': 20, 'red': 5, 'orange': 9}
2
'''
