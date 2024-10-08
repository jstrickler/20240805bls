from struct import Struct

puzzle_layout = 'fififhHfIdfdIiIh'
layout = Struct(puzzle_layout)

with open('../DATA/puzzle.data', 'rb') as puzzle_in:
    puzzle_data = puzzle_in.read()

    values = layout.unpack(puzzle_data)
    print(f"{values = }\n")
    

    bytes = [int(v) for v in  values]
    print(f"{bytes = }\n")
    
    name_letters = [chr(b) for b in bytes]
    print(f"{name_letters = }\n")
    
    print(''.join(name_letters))


# one-liner version -- just don't do this in production!!
print(''.join([chr(int(v)) for v in layout.unpack(open('../DATA/puzzle.data', 'rb').read())]))
