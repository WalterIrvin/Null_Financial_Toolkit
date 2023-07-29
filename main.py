import savings
import data_analytics


def interactive_savings_calculator():
    """ An interactive command line interface that allows comparisons between various saving strategies, and sees
    how they perform over a set year period.

    Commands: (Q)uit, (R)eset calculations, (C)ontinue calculation further

    :return:
    """
    saving_result = 0
    while 1:
        command = input("(Q)uit, (R)eset calculations, (C)ontinue calculation further: ")
        if command == "q" or command == "Q":
            break
        elif command == "r" or command == "R":
            saving_result = setup_comparison()
        elif command == "c" or command == "C":
            saving_result = setup_comparison(saving_result)
        else:
            print("Invalid command!")


def setup_comparison(starting=0):
    while 1:
        print(f"Starting from {starting}, enter the following details to get your report.")
        amount = int(input("Amount to save per year: "))
        bonus = int(input("Amount you can expect to get as bonus per year on top of what you make: "))
        rate = float(input("Interest rate per year: "))
        years = int(input("Number of years to calculate out for: "))
        print(f"Starting: {starting}, Amount: {amount}, Bonus: {bonus}, Rate: {rate}, Years: {years}")
        confirmation = input("Is this correct (Y/n): ")
        if confirmation == "n" or confirmation == "N":
            print("input discarded, retrying...\n")
        else:
            break
    simple_saving = savings.simple_saving_rate(starting, amount, years)
    complex_saving = data_analytics.salary_simple_savings(starting, amount, bonus, 100000, years)
    simple_interest = savings.simple_compound_saving_rate(starting, amount, years, rate)
    complex_interest = savings.complex_compound_saving_rate(starting, amount, bonus, years, rate)
    interest_amt = data_analytics.get_total_interest(starting, amount, bonus, rate, years)
    print("The results are as follows: ")
    print(f"Simple savings: {simple_saving}, Complex savings: {complex_saving}, "
          f"Simple interest: {simple_interest}, Complex interest: {complex_interest}, "
          f"Total interest gained: {interest_amt}")

    return complex_interest


if __name__ == '__main__':
    interactive_savings_calculator()

