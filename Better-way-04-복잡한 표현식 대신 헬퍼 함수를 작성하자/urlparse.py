from urllib.parse import parse_qs

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
