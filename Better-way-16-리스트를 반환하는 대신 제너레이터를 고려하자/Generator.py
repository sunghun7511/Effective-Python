# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 제너레이터를 사용하는 방법이 누적된 결과의 리스트를 반환하는 방법보다 이해하기에 명확하다.
* 제너레이터에서 반환하 이터레이터는 제너레이터 함수의 본문에 있는 yield 표현식에 전달된 값들의 집합이다.
* 제너레이터는 모든 입력과 출력을 메모리에 저장하지 않으므로 입력값의 양을 알기 어려울 때도 연속된 출력을 만들 수 있다.
'''

import itertools

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)
    return result

address = "Four score and seven yerars ago..."
result = index_words(address)
print(result[:3])

'''
[0, 5, 11]
'''


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


result = list(index_words_iter(address))
print(result)

'''
[0, 5, 11, 15, 21, 28]
'''


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset

with open("./address.txt", "r") as f:
    it = index_file(f)
    results = itertools.islice(it, 0, 3)
    print(list(results))

'''
[0, 5, 11]
'''
