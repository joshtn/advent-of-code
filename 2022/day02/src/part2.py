def advent():
    f = open('../input.txt', 'r')
    s = f.read()
    f.close()

    shape = {'R': 1, 'P': 2, 'S': 3}
    
    win = {'R': 'S', 'P': 'R', 'S': 'P'}

    loose = {'R': 'P', 'P': 'S', 'S': 'R'}

    trans = {
        'A': 'R', 'B': 'P', 'C': 'S',
        'X': 'L', 'Y': 'D', 'Z': 'W',
    }

# x=loose y=draw z=win
        
    for k, v in trans.items():         
        s = s.replace(k, v)

    n = 0
    for line in s.splitlines():
        a, b = line.split()
        if b == 'D':
            n += 3
            n += shape[a]
        elif b == 'W':
            n += 6
            n += shape[loose[a]]
        else:
            n += shape[win[a]]
        


    print(n)
    return n


advent()
