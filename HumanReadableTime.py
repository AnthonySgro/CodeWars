import math
def make_readable(seconds):
    hours = math.floor(seconds / 3600)
    remainder = seconds - hours * 3600
    minutes = math.floor(remainder / 60)
    seconds = remainder - minutes * 60
    
    
    show_hr = str(hours).zfill(2)
    show_min = str(minutes).zfill(2)
    show_sec = str(seconds).zfill(2)
        
    return show_hr + ":" + show_min + ":" + show_sec
