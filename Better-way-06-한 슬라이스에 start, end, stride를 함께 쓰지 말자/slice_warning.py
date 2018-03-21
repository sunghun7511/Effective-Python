# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 한 슬라이스에 start, end, stride를 지정하면 매우 혼란스러울 수 있다.
* 슬라이스에 start와 end  인덱스 없이 양수 stride 값을 사용하자. 음수 stride 값은 가느앟면 피하는 게 좋다.
* 한 슬라이스에 start, end, stride를 함께 사용하는 상황은 피하자. 파라미터 세 개를 사용해야 한다면 할당 두 개(하나는 슬라이스, 다른 하나는 스트라이드)를 사용하거나 내장 모듈 itertools의 islice를 사용하자.
'''

# stride : 간격

a = ["red", "orange", "yellow", "green", "blue", "purple"]

odds = a[::2]
evens = a[1::2]

print(odds)
print(evens)

'''
['red', 'yellow', 'blue']
['orange', 'green', 'purple']
'''


x = b"mongoose"
y = x[::-1]
print(y)

'''
b'esoognom'
'''

'''
w = "뷁뒑"
x = w.encode("utf-8")
y = x[::-1]
z = y.decode("utf-8")
'''

'''
Traceback (most recent call last):
  File ".\Better-way-06-한 슬라이스에 start, end, stride를 함께 쓰지 말자\slice_warning.py", line 28, in <module>
    z = y.decode("utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x91 in position 0: invalid start byte
'''


a = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(a[::2])
print(a[::-2])

'''
['a', 'c', 'e', 'g']
['h', 'f', 'd', 'b']
'''


print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])

'''
['c', 'e', 'g']
['g', 'e', 'c', 'a']
['g', 'e']
[]
'''

b = a[::2]
c = b[1:-1]

print(b)
print(c)

'''
['a', 'c', 'e', 'g']
['c', 'e']
'''
