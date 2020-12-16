def iq_test(numbers):
    
    numbers_list = numbers.split()
    
    even = False
    num_even = 0
    num_odd = 0
    
    #test first three numbers
    for n in range(0,3):
        if int(numbers_list[n]) % 2 == 1:
            num_odd += 1
        if int(numbers_list[n]) % 2 == 0:
            num_even += 1
    
    #even or odd list?
    if num_even > num_odd:
        even = True
    else:
        even = False
    
    #find the right index of our list
    for number in range(0,len(numbers_list)):
        if even == True:
            if int(numbers_list[number]) % 2 == 1:
                result = numbers_list[number]
                return numbers_list.index(result) + 1
        else:
            if int(numbers_list[number]) % 2 == 0:
                result = numbers_list[number]
                return numbers_list.index(result) + 1
