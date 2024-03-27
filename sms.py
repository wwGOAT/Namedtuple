class Fon:
    def __init__(self, massa: int, xotira: int):
        self.massa = massa
        self.xotira = xotira


    def __le__(self, other):
        if self.xotira > other.xotira:
            return "a kotta"

        elif self.xotira < other.xotira:
            return "b kotta"

        else:
            return "Teng"

a = Fon (10, 256)
b = Fon (10, 256)
print(a.__le__(b))


