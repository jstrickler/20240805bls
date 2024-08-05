value = 0

if value:
    print("crocodile")
elif value > 75:
    print("kangaroo")
    print("koala")
elif value > 50:  # else if
    print("wombat")
    print("wallaby")
elif value > 25:
    print("platypus")
    print("kookaburra")
else:
    print("tasmanian devil")

print("ALL DONE")


# x is false if
# x is None
# x is False
# x == 0
# len(x) == 0

while True:
    color = input("What is your favorite color? ")
    if color == 'q':
        break
    if color == '':
        continue
    print(f"You chose {color}")
