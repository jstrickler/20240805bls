person = "Taylor Swift"

print(f"{type(person) = }")
print(f"{person = }")  # repr()
print(person)

#  a-z _ 0-9 A-Z

person = "Mickey Mantle"

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['RDU'] = }")
KEY = 'LAX'
# print(f"{airports[KEY] = }")
print(f"{airports.get(KEY) = }")
print(f"{airports.get(KEY, 'NOT FOUND') = }")
print(f"{airports.get('MCI') = }")

print("Hello!")
a = "apple"
b = 123.49309203
print(a, b, sep=" / ")
print()

FILE_PATH = 'DATA/mary.txt'
with open(FILE_PATH) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print()

user_name = input("What is your name? ")
print(f"{user_name = }")

