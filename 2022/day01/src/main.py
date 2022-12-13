def advent1():
    f = open('../input.txt', 'r')
    x = f.read().split("\n")
    f.close()


    current_sum = 0
    elfs_cal_arr = []
    for _, value in enumerate(x):

        if not value:
            elfs_cal_arr.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(value)


    elfs_cal_arr.sort()
    top_3_cal = elfs_cal_arr[-3:]
    print(sum(top_3_cal))

advent1()
