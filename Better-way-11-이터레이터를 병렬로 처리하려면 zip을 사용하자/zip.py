# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 내장 함수 zip은 여러 이터레이터를 병렬로 순회할 때 사용할 수 있다.
* 파이썬 3의 zip은 튜플을 생성하는 지연 제너레이터다. 파이썬 2의 zip은 전체 결과를 튜플 리스트로 반환한다.
* 길이가 다른 이터레이터를 사용하면 zip은 그 결과를 조용히 잘라낸다.
* 내장 모듈 itertools의 zip_longest 함수를 쓰면 여러 이터레이터를 길이에 상관없이 병렬로 순회할 수 있다. (Better-way-46-내장 알고리즘과 자료구조를 사용하자 참고)
'''


names = ["Cecilia", "Lise", "Marie"]
letters = [len(n) for n in names]

print(names)
print(letters)

'''
['Cecilia', 'Lise', 'Marie']
[7, 4, 5]
'''


longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)

'''
Cecilia
'''


longest_name = None
max_letters = 0

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)

'''
Cecilia
'''


longest_name = None
max_letters = 0

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)

'''
Cecilia
'''


names.append("Rosalind")

for name, count in zip(names, letters):
    print(name)

'''
Cecilia
Lise
Marie
'''

# zip으로 실행할 리스트의 길이가 같다고 확신할 수 없다면 대신
# 내장 모듈 itertools의 zip_longest를 사용하는 방안을 고려해보자
# (파이썬 2에서는 izip_longest)