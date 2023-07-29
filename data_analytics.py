import savings


def get_total_interest(starting, amount, bonus, rate, years):
    """Gets the total gained from interest by subtracting the amount gained from simply saving at 0% gain

    :param starting: - starting amount
    :param amount: - amount that is added per year
    :param bonus: - amount to add on to amount per year
    :param rate: - yearly interest rate
    :param years: - how many years to calculate for
    :return total: - the total amount of purely interest grown (compared to just saving)
    """
    base_amount = savings.complex_saving_rate(starting, amount, bonus, years)
    interest_amount = savings.complex_compound_saving_rate(starting, amount, bonus, years, rate)
    total = interest_amount - base_amount
    return total
