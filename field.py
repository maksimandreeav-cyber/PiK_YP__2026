def field(items, *args):
    assert len(args) > 0
    count = len(args)
    for i in range(0, len(items)):
        m = {}
        n = 0
        for j in range(0, count):
            if args[j] in items[i] and items[i][args[j]] is not None:
                m[args[j]] = items[i][args[j]]
            if items[i][args[j]] is None:
                n += 1
        if len(args) == 1:
            yield m[args[0]]
        elif(n != count):
            yield m
