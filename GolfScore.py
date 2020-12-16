def golf_score_calculator(par_string, score_string):
    par_list = []
    score_list = []
    off_par_list = []
    
    for n in range(0, 18):
        par_list.append(int(par_string[n]))
        score_list.append(int(score_string[n]))
    
    for n in range(0, 18):
        off_par_list.append(score_list[n] - par_list[n])
    
    return sum(off_par_list)
