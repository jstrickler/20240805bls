
"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # sorted() returns a list

print(sorted_fruit)
print('-' * 60)

def ignore_case(s):
    compare_value = s.lower()
    print(f"comparing {s} as {compare_value}")
    return compare_value

s2 = sorted(fruits, key=ignore_case)
print(f"{s2 = }\n")

s3 = sorted(fruits, key=str.lower)
print(f"{s3 = }\n")

s4 = sorted(fruits, key=len)
print(f"{s4 = }\n")

def custom_sort(fruit):
    return len(fruit), fruit.lower()  # return tuple

s5 = sorted(fruits, key=custom_sort)
print(f"{s5 = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

n1 = sorted(nums)
print(f"{n1 = }\n")

n2 = sorted(nums, key=str)
print(f"{n2 = }\n")

s6 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print(f"{s6 = }\n")

# lambda p1, ...: return-value (based on params)

# lambda : 0

