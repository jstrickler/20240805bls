from functools import wraps
from datetime import datetime

def timestamp(original_function):

    @wraps(original_function)
    def _replacement(*pos, **named):
        print(datetime.now().ctime())
        result = original_function(*pos, **named)
        return result
    
    return _replacement


@timestamp
def spam(color):
    print("spam!")
# spam = timestamp(spam)
#  really, spam = _replacement

@timestamp
def ham(value1, value2):
    print("ham!")

spam("blue")
ham(5, 10)

print(spam.__name__)
print(ham.__name__)