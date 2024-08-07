
#  type("name", (base_class,), {attrs})

Animal = type("Animal", (), {})
print(f"{Animal = }")
a  = Animal()
print(f"{a = }\n")

def bark(self):
    print("woof! woof!")

Dog = type("Dog", (Animal,), {"bark": bark})

d = Dog()
d.bark()
print(f"{d = }")
