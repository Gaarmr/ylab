class CyclicIterator:
    def __init__(self, i):
        self._buffer = []
        self._iter_depleted = False
        self._iter = iter(i)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self._iter)
            if not self._iter_depleted:
                self._buffer.append(item)
            return item
        except StopIteration:
            self._iter_depleted = True
            self._iter = iter(self._buffer)
            return self.__next__()


# cyclic_iterator = CyclicIterator(range(3))


# for i in cyclic_iterator:
#     print(i)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()  
myiter = iter(myclass)  

for i in CyclicIterator(MyNumbers()):
    pass