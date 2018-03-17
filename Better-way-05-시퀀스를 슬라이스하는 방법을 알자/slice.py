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