def how_many_times(annual_price, individual_price):
    amount_by_year = int(annual_price / individual_price)
    
    if annual_price % individual_price == 0:
        return amount_by_year
    else:
        return amount_by_year + 1
