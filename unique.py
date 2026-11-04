class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = items
        self.seen = set()
        self.iter = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            item = next(self.iter)
            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self

#print( list(Unique(['1', 'A', 'b', 'B', 'a'], a = 122, ignore_case = True)))
