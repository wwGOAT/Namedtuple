class Eldor:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = - step
            self.stop = start
            self.step = step
        else:
            if start < stop:
                if step > 0:
                    self.start = start - step
                    self.stop = stop
                    self.step = step
                else:
                    self.start = start + step
                    self.stop = stop
                    self.step = step

            elif start > stop:
                if step > 0:
                    self.start = start + step
                    self.stop = stop
                    self.step = step
                else:
                    self.start = start - step
                    self.stop = stop
                    self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop > self.start:
            if self.step > 0:
                self.start += self.step
                if self.start >= self.stop:
                    raise StopIteration
                return self.start
            else:
                self.start -= self.step
                if self.start >= self.stop:
                    raise StopIteration
                return self.start
        else:
            if self.step > 0:
                self.start -= self.step
                if self.start <= self.stop:
                    raise StopIteration
                return self.start
            else:
                self.start += self.step
                if self.start <= self.stop:
                    raise StopIteration
                return self.start


for i in Eldor(12, 1, 9 ):
    print(i)