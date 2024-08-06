fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f0 = []
for f in fruits:
    value = f.lower()
    f0.append(value)
print(f"{f0 = }\n")

#   [value for var in iterable if condition]
f1 = [f.lower() for f in fruits]
print(f"{f1 = }\n")

f2 = [f.lower() for f in fruits if len(f) > 8]
print(f"{f2 = }\n")

f3 = [f.lower() for f in fruits if f.lower().startswith('p')]
print(f"{f3 = }\n")

f4 = [f for f in fruits if f.lower().startswith('p')]
print(f"{f4 = }\n")

with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines()   # read file and split into lines without end-of-line chars

print(f"{foods = }\n")

nonspam = [food for food in foods if food != 'spam']

print(f"{nonspam = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [person[3] for person in people]
print(f"{dobs = }\n")




