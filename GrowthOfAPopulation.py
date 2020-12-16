def nb_year(p0, percent, aug, p):
    counter = 0
    while p0 < p:
        p0 = p0 + p0 * percent / 100 + aug
        counter += 1
    return counter
