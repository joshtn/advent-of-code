def advent():
    f = open('../input.txt', 'r')
    s = f.read()
    f.close()

    sum = 0

    items = iter(s.splitlines())
    while True:
        try:
            s, = set(next(items)) & set(next(items)) & set(next(items))
        except StopIteration:
            break
        else:
            if s.islower():
                sum += 1 + (ord(s) - ord('a'))
            elif s.isupper():
                sum += 27 + (ord(s) - ord('A'))

    print(sum)
    return sum



advent()
