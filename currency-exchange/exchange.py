def exchange_money(budget, exchange_rate):
    budget = float(budget) 
    exchange_rate = float(exchange_rate)
    
    new_rate = budget / exchange_rate
    return new_rate



def get_change(budget, exchanging_value):
    change = budget - exchanging_value

    return change


def get_value_of_bills(denomination, number_of_bills):
    value = number_of_bills * denomination
    
    return int(value)


def get_number_of_bills(budget, denomination):
    budget = float(budget)
    denomination = int(denomination)
    
    number_of_bills = budget / denomination

    return int(number_of_bills)


def get_leftover_of_bills(budget, denomination):
    leftover = budget % denomination
    return leftover



def exchangeable_value(budget, exchange_rate, spread, denomination):
    budget = float(budget)
    exchange_rate = float(exchange_rate)
    spread = float(spread)
    spread = spread / 100
    real_rate = exchange_rate + (exchange_rate * spread)
    value = budget / real_rate
    leftover = (value % denomination)
    newValue = value - leftover
    
    return newValue
