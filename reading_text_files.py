with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:  # iterate over the file object
        print(raw_line.rstrip())
