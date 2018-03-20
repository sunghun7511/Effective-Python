a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''


squares = map(lambda x : x ** 2, a)
print(list(squares))

'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''


even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

'''
[4, 16, 36, 64, 100]
'''


alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
alt_lst = list(alt)
assert even_squares == alt_lst

print(alt_lst)

'''
[4, 16, 36, 64, 100]
'''


chile_ranks = {"ghost": 1, "habanero": 2, "cayenne": 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}

print(rank_dict)
print(chile_len_set)

'''
{1: 'ghost', 2: 'habanero', 3: 'cayenne'}
{8, 5, 7}
'''
