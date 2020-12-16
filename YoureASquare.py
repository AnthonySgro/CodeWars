def is_square(n):    
    if n == 0:
        return True
    elif n > 0:
        if (n ** .5) % 1 != 0:
            return False
        else:
            return True
    else:
        return False
