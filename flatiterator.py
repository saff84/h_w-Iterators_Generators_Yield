class FlatIterator:

    def __init__(self, list):
        self.indx = 0
        self.list = [item for i in list for item in i]

    def __iter__(self):

        return self

    def __next__(self):

        if self.indx == len(self.list):
            raise StopIteration

        val = self.list[self.indx]

        self.indx += 1
        return val
