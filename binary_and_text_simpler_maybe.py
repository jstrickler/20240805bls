
a = "5\u00B0"
print(a)
print(f"{a[0] = }")
print(f"{a[1] = }")
print()

b = a.encode()
print(b)
print(f"{b[0] = }")
print(f"{b[1] = }")
print(f"{b[2] = }")
