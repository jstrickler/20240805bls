import random
FILE_PATH = "DATA/words.txt"

class RandomWord:
    def __init__(self):
        self._words = open(FILE_PATH).read().splitlines()

    def __call__(self):
        return random.choice(self._words)

if __name__ == "__main__":
    rw = RandomWord()
    for _ in range(10):
        print(rw())
