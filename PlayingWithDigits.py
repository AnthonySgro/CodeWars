def dig_pow(n, p):
    digits_list = list(str(n))

    counter = 0
    running_sum = 0
    success = False

    for x in range(0, len(digits_list)):
        running_sum += int(digits_list[x]) ** p
        p += 1
        counter += 1
        if counter == len(digits_list):
            for k in range(0, 1000000):
                if running_sum == n * k:
                    success = True
                    return k
            if success == False:
                return -1
