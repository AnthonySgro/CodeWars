def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    solutions = []
    
    #iterate through the range
    for num in range(a, b + 1):
        string_num = str(num)
        digits = []
        
        #make a list of the digits
        for digit in string_num:
            digits.append(int(digit))
             
        #Get sum of its digits
        #Raised to consecutive powers
        counter = 0
        sum = 0
        for digit in digits:
            counter += 1
            sum += digit ** counter
        
        #If solution, add to list
        if sum == num:
            solutions.append(num)
            
    return solutions
