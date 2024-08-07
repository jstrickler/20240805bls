cities = list()       #    list cities = new list();
cities.append("Fairfax")
cities.append("Clifton")
cities.append("Tacoma")
cities.append("Annandale")
cities.insert(3, "Woodbridge")
cities.insert(0, "Silver Spring")
print(f"{cities = }\n")

n = 15    #  n = int(15)      int n = 15;

print(f"{type(cities) = }")
print(f"{type(n) = }")

# conn = mssql.connect(...)
# response = requests.get('https://www.bls.gov')

class Animal:
    def breathe(self):
        print("breathing...")

fred_the_frog = Animal()
fred_the_frog.breathe()
print()

class Dog(Animal):
    def bark(self):
        print("Woof! woof!")

nellie = Dog()
nellie.bark()
nellie.breathe()
