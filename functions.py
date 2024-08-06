def hello():
    print("Hello, world")

hello()
print()

def greet(whom="world"):
    print(f"Hello, {whom}")

greet("New York")
greet("world")
greet("hungry, hungry hippos")
greet()
print()

person = "Dick Van Dyke"
greet(person)
print()

def double(x):
    return x * 2

r1 = double(8)
print(f"{r1 = }")
r2 = double("mint")
print(f"{r2 = }")

r3 = 5 + double(x=9.839)
print(f"{r3 = }")
print()

h = hello()
print(f"{h = }")
print()

def grep_lines(search_term, *file_paths, ignore_case=True):
    print(f"{file_paths = }\n")
    
    if ignore_case:
        search_term = search_term.lower()
    lines = []
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if ignore_case:
                    line_to_search = raw_line.lower()
                else:
                    line_to_search = raw_line
                if search_term in line_to_search:
                    lines.append(raw_line.rstrip())
    return lines

found_lines = grep_lines("bird", "DATA/alice.txt", "DATA/parrot.txt")
for line in found_lines:
    print(line)
print('-' * 60)

found_lines = grep_lines("lizard", "DATA/alice.txt", "DATA/parrot.txt", "DATA/words.txt", ignore_case=False)
for line in found_lines:
    print(line)
print('-' * 60)




