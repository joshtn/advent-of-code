def advent1():
    f = open('../input.txt', 'r')
    x = f.read().split("\n")
    f.close()


    largest_cal = 0
    current_sum = 0
    for _, value in enumerate(x):

        if not value:
            largest_cal = max(largest_cal, current_sum)
            current_sum = 0
        else:
            current_sum += int(value)


    print(largest_cal)

advent1()
