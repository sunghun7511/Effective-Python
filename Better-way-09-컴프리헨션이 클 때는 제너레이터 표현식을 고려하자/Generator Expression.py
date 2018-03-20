value = [len(x) for x in open("/tmp/my_file.txt")]
print(value)

'''
[2, 3, 3, 5, 4, 1]
'''


it = (len(x) for x in open("/tmp/my_file.txt"))
print(it)

'''
<generator object <genexpr> at 0x7f8cef0adf68>
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
