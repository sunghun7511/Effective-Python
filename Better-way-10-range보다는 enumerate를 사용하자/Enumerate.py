# -*- coding: utf-8 -*-
import random

'''
## 핵심 정리

* enumerate는 이터레이터를 순회하면서 이터레이터에서 각 아이템의 인덱스를 얻어오는 간결한 문법을 제공한다.
* range로 루프를 실행하고 시퀀스에 인덱스로 접근하기보다는 enumerate를 사용하는 게 좋다.
* enumerate에 두 번재 파라미터를 사용하면 세기 시작할 숫자를 지정할 수 있다.(기본값은 0이다.)
'''


random_bits = 0

for i in range(64):
    if random.randint(0, 1):
        random_bits |= 1 << i

print(random_bits)

'''
16524791927133437967
'''


flavor_list = ["vanila", "chocolate", "pecan", "strawberry"]
for flavor in flavor_list:
    print("%s is delicious" % flavor)

'''
vanila is delicious
chocolate is delicious
pecan is delicious
strawberry is delicious
'''


for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print("%d : %s" % (i + 1, flavor))

'''
1 : vanila
2 : chocolate
3 : pecan
4 : strawberry
'''


for i, flavor in enumerate(flavor_list):
    print("%d : %s" % (i + 1, flavor))

'''
1 : vanila
2 : chocolate
3 : pecan
4 : strawberry
'''
