def simple_saving_rate(starting, amount, years):
    """A simplistic model that adds up your total savings gained from a yearly rate and number of years saving.
    no interest accured, basically equivalent to putting directly into a bank and not touching it.

    :param starting: - starting amount
    :param amount: - yearly amount of USD
    :param years: - years saving at this rate
    :return: - amount * number of years
    """
    return starting + (amount * years)


def complex_saving_rate(starting, amount, bonus_per_year, years):
    """More complex savings strategy, still does not use compound interest, but instead relies on our
    fixed saving amount going up each year (to account for inflation/promotions/bonuses)

    :param starting: - starting amount in USD
    :param amount: - amount saved each year
    :param bonus_per_year: - amount to add to our saving total per year
    :param years: - amount of years to calculate
    :return total: - total amount in USD after the final year, accounting for the bonuses per year
    """
    total = starting
    for i in range(years):
        total += amount
        amount += bonus_per_year
    return total


def simple_compound_saving_rate(starting, amount, years, interest_rate):
    """More complex saving model, starting from set amount, a fixed rate is added over number of years, with the
    interest rate determining the amount of compounding interest.

    :param starting: - starting amount in USD
    :param amount: - fixed amount saved per year
    :param years: - amount of years to calculate
    :param interest_rate: - percentage rate the total will go up by
    :return total: - total amount in USD after the final year, accounting for compound interest and savings.
    """
    total = starting
    for i in range(years):
        total += amount
        total += total * interest_rate
    return total


def complex_compound_saving_rate(starting, amount, bonus_per_year, years, interest_rate):
    """More complex saving model, starting from a set amount, a gradually increasing amount is added over a number
    of years, with a fixed compounding interest rate applied yearly.

    :param starting: - starting amount in USD
    :param amount: - amount to save per year
    :param bonus_per_year: - amount to add to our saving total per year
    :param years: - amount of years to calculate
    :param interest_rate: - percentage rate that we recieve in interest per year
    :return total: - total calculated after increasing savings rate per year with compounding interest.
    """
    total = starting
    for i in range(years):
        total += amount
        amount += bonus_per_year
        total += total * interest_rate
    return total

