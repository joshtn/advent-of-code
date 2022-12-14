def advent():
    f = open('../input.txt', 'r')
    s = f.read()
    f.close()

    shape = {'R': 1, 'P': 2, 'S': 3}
    
    win = {'R': 'S', 'P': 'R', 'S': 'P'}

    trans = {
        'A': 'R', 'B': 'P', 'C': 'S',
        'X': 'R', 'Y': 'P', 'Z': 'S',
    }
        
#making abc xyx into only rps
    for k, v in trans.items():         
        s = s.replace(k, v)

#calculate
    n = 0
    for line in s.splitlines():
        a, b = line.split()
        if a == b:
            n += 3
        elif win[a] != b:
            n += 6
        else:
            pass
        
        n += shape[b]

    print(n)
    return n


advent()
