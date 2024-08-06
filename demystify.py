FILE_PATH = "mystery"

with open(FILE_PATH, 'rb') as mystery_in:
    while True:
        chunk = mystery_in.read(3)
        if len(chunk) == 0:
            break
        print(  chr(chunk[2]),    end="")
