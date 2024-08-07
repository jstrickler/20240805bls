"""
Weird Python Magic
"""
x = 100

person = "Dean Martin"


def spam():
    print("spam spam spam spam")

class Ham:
    pass

g = globals()
print(g['x'])
print(g['person'])

s = g['spam']
s()

g['color'] = 'blue'
print(color)

def toast():
    a = 'apple'
    b = 'banana'
    c = "lemon"
    print(f"{locals() = }")

toast()
print()
print(g)






