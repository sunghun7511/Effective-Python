import random

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
