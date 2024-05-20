class Repeat:
    def __init__(self, value):
        self.__value = value

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.__value
    
xs = Repeat(5)

print(next(xs))
print(next(xs))
print(xs)