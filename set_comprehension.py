colors = ['red', 'green', 'Navy', 'BLACK', 'Pink', 'purple', 'orange', 'brown',
'black', 'RED', 'olive', 'navy', 'white', 'black', 'black', 'brown', 'brown', 'orange',
'pink', 'blue', 'BLUE', 'Blue', 'BLUE', 'chartreuse']

s1 = set(colors)
print(f"{s1 = }\n")

s2 = {c.lower() for c in colors}
print(f"{s2 = }\n")

