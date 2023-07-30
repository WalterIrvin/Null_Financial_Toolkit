import data_analytics
import panel as pn


def interactive_savings_calculator():
    """ An interactive command line interface that allows comparisons between various saving strategies, and sees
    how they perform over a set year period.

    Commands: (Q)uit, (R)eset calculations, (C)ontinue calculation further

    :return:
    """
    saving_result = 0
    while 1:
        command = input("(Q)uit, (C)ontinue calculation further: ")
        if command == "q" or command == "Q":
            break
        elif command == "c" or command == "C":
            setup_comparison(saving_result)
        else:
            print("Invalid command!")


def setup_comparison(starting=0):
    while 1:
        print(f"Starting from {starting}, enter the following details to get your report.")
        amount = int(input("Amount to save per year: "))
        bonus = int(input("Amount you can expect to get as bonus per year on top of what you make: "))
        cap = int(input("Amount your field tends to cap out on salary: "))
        rate = float(input("Interest rate per year: "))
        years = int(input("Number of years to calculate out for: "))
        print(f"Starting: {starting}, Amount: {amount}, Bonus: {bonus}, Cap: {cap}, Rate: {rate}, Years: {years}")
        confirmation = input("Is this correct (Y/n): ")
        if confirmation == "n" or confirmation == "N":
            print("input discarded, retrying...\n")
        else:
            break
    data_analyser = data_analytics.DataAnalysis(starting, amount, bonus, cap, rate)
    data_analyser.print_report(years)


if __name__ == '__main__':
    template = pn.template.FastListTemplate(title="Financial Toolkit")
    template.servable()
    template.show()
    #interactive_savings_calculator()

