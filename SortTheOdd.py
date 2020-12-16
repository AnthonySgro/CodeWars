def sort_array(source_array):
    if sum(source_array) == 0:
        return source_array
    
    else:
        even_or_odd = []
        odds = []
        
        for int in source_array:
            if int % 2 == 1:
                even_or_odd.append("o")
                odds.append(int)
            else:
                even_or_odd.append("e")
                
        odds.sort()
        
        counter = 0
        for num in range(0, len(source_array)):
            if even_or_odd[num] == "o":
                source_array[num] = odds[counter]
                counter += 1

        return source_array
