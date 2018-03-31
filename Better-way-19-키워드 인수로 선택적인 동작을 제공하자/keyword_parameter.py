# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 함수의 인수를 위치나 키워드로 지정할 수 있다.
* 위치 인수만으로는 이해하기 어려울 때 키워드 인수를 쓰면 각 인수를 사용하는 목적이 명확해진다.
* 키워드 인수에 기본값을 지정하면 함수에 새 동작을 쉽게 추가할 수 있다. 특히, 함수를 호출하는 기존 코드가 있을 때 사용하면 좋다.
* 선택적인 키워드 인수는 항상 위치가 아닌 키워드로 넘겨야 한다.
'''

def remainder(number, divisor):
    return number % divisor

print(remainder(20, 7))

'''
6
'''


print(remainder(20, 7))
print(remainder(20, divisor=7))
print(remainder(number=20, divisor=7))
print(remainder(divisor=7, number=20))

'''
6
6
6
6
'''


# remainder(number=20, 7)
# 위치 인수는 키워드 인수 앞에 지정해야 한다.

# remainder(20, number=7)
# 각 인수는 한 번만 지정할 수 있다.

def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print("%.3f kg per second" % flow)

'''
0.167 kg per second
'''

def flow_rate_time(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


flow_per_second = flow_rate_time(weight_diff, time_diff, 1)
flow_per_second = flow_rate_time(weight_diff, time_diff)

flow_per_hour = flow_rate_time(weight_diff, time_diff, period=3600)

print("%.3f kg per second" % flow_per_second)
print("%.3f kg per hour" % flow_per_hour)

'''
0.167 kg per second
600.000 kg per hour
'''


def flow_rate_edit(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff) * period


pounds_per_hour = flow_rate_edit(weight_diff, time_diff, period=3600, units_per_kg=2.2)

# 여전히 위치 인수로 넘길 수 있다.
pounds_per_hour = flow_rate_edit(weight_diff, time_diff, 3600, 2.2)

print(pounds_per_hour)

'''
272.72727272727275
'''