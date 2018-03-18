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
