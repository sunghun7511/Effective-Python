# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 리스트 컴프리헨션은 큰 입력을 처리할 때 너무 많은 메모리를 소모해서 문제를 일으킬 수 있다.
* 제너레이터 표현식은 이터레이터로 한 번에 한 출력만 만드므로 메모리 문제를 피할 수 있다.
* 한 제너레이터 표현식에서 나온 이터레이터를 또 다른 제네레이터 표현식의 for 서브표현식으로 넘기는 방식의 제너레이터 표현식을 조합할 수 있다.
* 제너레이터 표현식은 서로 연결되어 있을 때 매우 빠르게 실행된다.
'''


value = [len(x) for x in open("./my_file.txt")]
print(value)

'''
[4, 8, 4, 5, 7, 1]
'''


it = (len(x) for x in open("/tmp/my_file.txt"))
print(it)

'''
<generator object <genexpr> at 0x7f67a3e83960>
'''


print(next(it))
print(next(it))

'''
2
3
'''


roots = ((x, x**0.5) for x in it)
print(next(roots))

'''
(3, 1.7320508075688772)
'''
