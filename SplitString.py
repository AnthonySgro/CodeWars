def solution(s):
    list = []
    if len(s) == 0:
        return list
    elif len(s) % 2 == 0:
        for n in range(0, len(s), 2):
            list.append(s[n] + s[n+1])
        return list
    else:
        for n in range(0, len(s)-2, 2):
            list.append(s[n] + s[n+1])
        list.append(s[len(s)-1] + "_")
        return list
