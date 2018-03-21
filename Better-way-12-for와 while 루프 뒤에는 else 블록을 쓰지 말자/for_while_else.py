# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 파이썬에는 for와 whiile 루프의 내부 블록 바로 뒤에 else 블록을 사용할 수 있게 하는 특별한 문법이 있다.
* 루프 본문이 break 문을 만나지 않은 경우에만 루프 다음에 오는 else 블록이 실행된다.
* 루프 뒤에 else 블록을 사용하면 직관적이지 않고 혼동하기 쉬우니 사용하지 말아야 한다.
'''


for i in range(3):
    print("Loop %d" % i)
else:
    print("Else block!")

'''
Loop 0
Loop 1
Loop 2
Else block!
'''


for i in range(3):
    print("Loop %d" % i)
    if i == 1:
        break
else:
    print("Else block!")

'''
Loop 0
Loop 1
'''


for x in []:
    print("Never runs")
else:
    print("For else block!")

'''
For else block!
'''


while False:
    print("Never runs")
else:
    print("While else block!")

'''
While else block!
'''


a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print("Testing", i)
    if a % i == 0 and b % i == 0:
        print("Not compire")
        break
else:
    print("Compire")

'''
Testing 2
Testing 3
Testing 4
Compire
'''


def compire(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def compire2(a, b):
    is_compire = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_compire = False
            break
    return is_compire