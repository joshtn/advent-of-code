def advent():
    f = open('../input.txt', 'r')
    s = f.read()
    f.close()

    shape = {'R': 1, 'P': 2, 'S': 3}
    
    win = {'R': 'S', 'P': 'R', 'S': 'P'}

    loose = {v: k for k, v in win.items()}

    trans = {'A': 'R', 'B': 'P', 'C': 'S'}


    # x=loose y=draw z=win
        
    for k, v in trans.items():         
        s = s.replace(k, v)

    n = 0
    for line in s.splitlines():
        a, b = line.split()
        if b == 'Y':
            n += shape[a] + 3
        elif b == 'Z':
            n += shape[loose[a]] + 6
        else:
            n += shape[win[a]]
        


    print(n)
    return n


advent()
