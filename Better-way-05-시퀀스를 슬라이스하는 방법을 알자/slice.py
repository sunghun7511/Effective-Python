# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 너무 장황하지 않게 하자. 즉, start 인덱스에 0을 설정하거나 end 인덱스에 시퀀스의 길이를 설정하지 말자.
* 슬라이싱은 범위를 벗어난 start나 end 인덱스를 허용하므로 a[:20]이나 a[-20]처럼 시퀀스의 앞쪽이나 뒤쪽 경계에 놓인 슬라이스를 표현하기가 쉽다.
* list 슬라이스에 할당하면 원본 시퀀스에 지정한 범위를 참조 대상의 내용으로 대체한다.(길이가 달라도 동작한다.)
'''


a = ["a", "b", "c", "d", "e", "f", "g", "h"]

print("First four : ", a[:4])
print("Last four : ", a[-4:])
print("Middle two : ", a[3:-3])

'''
First four :  ['a', 'b', 'c', 'd']
Last four :  ['e', 'f', 'g', 'h']
Middle two :  ['d', 'e']
'''


assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

# first_twenty_items = a[:20]
# last_twenty_items = a[-20:]

'''
'''


b = a[4:]
print("Before :     ", b)
b[1] = 99
print("After :      ", b)
print("No change :  ", a)

'''
Before :      ['e', 'f', 'g', 'h']
After :       ['e', 99, 'g', 'h']
No change :   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
'''


print("Before :     ", a)
a[2:7] = [99, 22, 14]
print("After :      ", a)

'''
Before :      ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
After :       ['a', 'b', 99, 22, 14, 'h']
'''


b = a[:]
assert b == a and b is not a

'''
'''


b = a
print("Before :     ", a)
a[:] = [101, 102, 103]
assert a is b
print("After :      ", a)

'''
Before :      ['a', 'b', 99, 22, 14, 'h']
After :       [101, 102, 103]
'''