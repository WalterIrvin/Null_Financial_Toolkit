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


def salary_growth_calculator(starting, bonus, years, cap):
    """More realistic salary growth curve, where there is ultimately a limit to how much can be made, meaning
    bonus will not apply once the cap is reached.

    :param starting: - the starting point for salary
    :param bonus: - expected growth in salary per year of experience
    :param years: - years working
    :param cap: - the salary ceiling for the particular field
    :return amount: - the salary expected after the number of years input
    """
    total = starting
    for i in range(years):
        if total + bonus < cap:
            total += bonus
        else:
            return cap
    return total


def salary_simple_savings(starting, amount, bonus, cap, years):
    """Returns the total amount gained by salary with no interest rate.

    :param starting:
    :param amount:
    :param bonus:
    :param cap:
    :param years:
    :return:
    """
    total = starting
    cur_salary = amount
    for i in range(years):
        total += cur_salary
        cur_salary = salary_growth_calculator(cur_salary, bonus, years, cap)
    return total


def salary_interest_savings(starting, amount, bonus, cap, rate, years):
    """Gets total amount of savings generated with fixed interest rate, implemented with a cap on total salary.

    :param starting: - starting point for savings
    :param amount: - amount of salary currently gained
    :param bonus: - amount expected to rise per year on salary
    :param cap: - total amount salary can raise to
    :param rate: - interest rate per year
    :param years: - years to calculate for
    :return total: - total amount saved with capped salary and interest
    """
    total = starting
    cur_salary = amount
    for i in range(years):
        total += cur_salary
        total += total * rate
        cur_salary = salary_growth_calculator(cur_salary, bonus, 1, cap)
    return total


def salary_interest_savings_total_interest(starting, amount, bonus, cap, rate, years):
    """Calculates total interest generated over specified years given a salary with a cap, and fixed interest rate.

    :param starting: - starting point for savings
    :param amount: - amount of salary currently gained
    :param bonus: - amount expected to rise per year on salary
    :param cap: - total amount salary can raise to
    :param rate: - interest rate per year
    :param years: - years to calculate for
    :return total: - total amount of interest generated
    """
    interest_amount = starting
    base_amount = starting
    cur_salary = amount
    for i in range(years):
        base_amount += savings.simple_saving_rate(base_amount, cur_salary, 1)
        interest_amount += savings.simple_compound_saving_rate(interest_amount, cur_salary, 1, rate)
        cur_salary = salary_growth_calculator(cur_salary, bonus, 1, cap)

    total = interest_amount - base_amount
    return total
