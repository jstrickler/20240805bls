
class Spam:

    def __getitem__(self, index):
        """
        Implement the [] operation on objects of type Spam
        """
        return index * 2

    def __add__(self, other):
        return 42

s = Spam()
print(s[5])

x = Spam()
print(s + x)



