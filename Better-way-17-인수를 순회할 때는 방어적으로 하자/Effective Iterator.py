# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 입력 인수를 여러 번 순회하는 함수를 작성할 때 주의하자. 입력 인수가 이터레이터라면 이상하게 동작해서 값을 잃어버릴 수 있다.
* 파이썬의 이터레이터 프로토콜은 컨테이너와 이터레이터가 내장 함수 iter, next와 for 루프 및 관련 표현식과 상호 작용하는 방법을 정의한다.
* __iter__ 메서드를 제너레이터로 구현하면 자신만의 이터러블 컨테이너 타입을 쉽게 정의할 수 있다.
* 어떤 값 iter를 두 번 호출했을 때 같은 결과가 나오고 내장 함수 next로 전진시킬 수 있다면 그 값은 컨테이너가 아닌 이터레이터다.
'''

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

'''
[11.538461538461538, 26.923076923076923, 61.53846153846154]
'''


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits("./my_numbers.txt")
percentages = normalize(it)
print(percentages)

'''
[]
'''


it = read_visits("./my_numbers.txt")
print(list(it))
print(list(it))

'''
[15, 35, 80]
[]
'''


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


it = read_visits("./my_numbers.txt")
percentages = normalize_copy(it)
print(percentages)

'''
[11.538461538461538, 26.923076923076923, 61.53846153846154]
'''


path = "./my_numbers.txt"

def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


percentages = normalize_func(lambda: read_visits(path))
print(percentages)

'''
[11.538461538461538, 26.923076923076923, 61.53846153846154]
'''


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path
    
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)

'''
[11.538461538461538, 26.923076923076923, 61.53846153846154]
'''


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError("Must supply a container")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
print(normalize_defensive(visits))

visits = ReadVisits(path)
print(normalize_defensive(visits))

it = iter(visits)
print(normalize_defensive(it))

'''
[11.538461538461538, 26.923076923076923, 61.53846153846154]
[11.538461538461538, 26.923076923076923, 61.53846153846154]
Traceback (most recent call last):
  File "Effective Iterator.py", line 123, in <module>
    normalize_defensive(it)
  File "Effective Iterator.py", line 108, in normalize_defensive
    raise TypeError("Must supply a container")
TypeError: Must supply a container
'''