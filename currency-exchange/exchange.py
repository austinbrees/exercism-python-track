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
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    pass


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    pass
