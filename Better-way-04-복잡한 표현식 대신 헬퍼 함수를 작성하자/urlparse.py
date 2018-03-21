# -*- coding: utf-8 -*-
from urllib.parse import parse_qs

'''
## 핵심 정리

* 파이썬의 문법을 이용하면 한 줄짜리 표현식을 쉽게 작성할 수 있지만 코드가 복잡해지고 읽기 어려워진다.
* 복잡한 표현식은 헬퍼  함수로 옮기는 게 좋다. 특히, 같은 로직을 반복해서 사용해야 한다면 헬퍼 함수를 사용하자.
* if/else 표현식을 이용하면 or나 and 같은 불 연산자를 사용할 때보다 읽기 수월한 코드를 작성할 수 있다.
'''


my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

print(repr(my_values))

'''
'''


print("Red:     ", my_values.get("red"))
print("Green:   ", my_values.get("green"))
print("Opacity: ", my_values.get("opacity"))

'''
Red:      ['5']
Green:    ['']
Opacity:  None
'''


red = my_values.get("red", [""])[0] or 0
green = my_values.get("green", [""])[0] or 0
opacity = my_values.get("opacity", [""])[0] or 0

print("Red:     %r" % red)
print("Green:   %r" % green)
print("Opacity: %r" % opacity)

'''
Red:     '5'
Green:   0
Opacity: 0
'''

red = int(my_values.get("red", [""])[0] or 0)

'''
'''


red = my_values.get("red", [""])
red = int(red[0]) if red[0] else 0

'''
'''


# Helper function
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green = get_first_int(my_values, "green")
