def advent():
    f = open('../input.txt', 'r')
    s = f.read()
    f.close()

    sum = 0

    lines = s.splitlines()
    for line in lines:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        s, = set(first_half) & set(second_half)
        if s.islower():
            sum += 1 + (ord(s) - ord('a'))
        elif s.isupper():
            sum += 27 + (ord(s) - ord('A'))

    print(sum)
    return sum



advent()
