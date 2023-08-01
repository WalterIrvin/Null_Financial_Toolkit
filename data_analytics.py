import panel as pn
import pandas as pd
import hvplot.pandas


def salary_growth(years, income, bonus, cap):
    """Helper function to calculate salary after x years of growth to a specified cap value.

    :param years: - number of years to calculate out for.
    :param income: - amount of income to start at.
    :param bonus: - amount expected to gain per year.
    :param cap: - total ceiling of income expected.
    :return: - total salary or the cap
    """
    salary = income
    for i in range(years):
        if salary + bonus < cap:
            salary += bonus
        else:
            return cap
    return salary


def growth(starting, years, income=0, bonus=0, cap=0, interest=0):
    """Helper function to calculate growth of savings after x amount of years given interest, salary, etc.

    :param starting: - starting value for savings.
    :param years: - years to calculate out for.
    :param income: - starting income for calculation.
    :param bonus: - amount expected to gain per year to yearly contribution.
    :param cap: - total ceiling of income expected.
    :param interest: - interest rate per year on total savings.
    :return [total, base]: - A list containing total amount of savings at the end, plus the amount contributed.
    """
    base = starting
    total = starting
    salary = income
    for i in range(years):
        total += salary
        base += salary
        salary = salary_growth(i, salary, bonus, cap)
        total += total * interest
    return [total, base]


class DataAnalysis:
    def __init__(self):
        """A data analysis class that will calculate savings growth expected after x amount of years given
        various factors that play into portfolio growth: starting funds, income, income growth, income cap,
        interest rate, and years to calculate for. All fields are configurable by the sidebar inputs, which are
        then propagated to the dataframe and used to update the graphs with various useful information.

        :attribute starting: - float input for the starting funds.
        :attribute salary: - float input for the starting income.
        :attribute salary_bonus: - float input for yearly expected growth in income.
        :attribute salary_cap: - float input for expected cap in yearly income.
        :attribute interest_rate: - float input for yearly interest on money.
        :attribute years: - int input for years to calculate for.
        :attribute dataframe: - dataframe holding all useful info of this class, which can be exported to csv.
        """
        self.starting = pn.widgets.FloatInput(name="Starting funds")
        self.salary = pn.widgets.FloatInput(name="Income")
        self.salary_bonus = pn.widgets.FloatInput(name="Bonus per year")
        self.salary_cap = pn.widgets.FloatInput(name="Income Ceiling")
        self.interest_rate = pn.widgets.FloatInput(name="Interest rate")
        self.years = pn.widgets.IntInput(name="Years")
        self.dataframe = pd.DataFrame()
        self.update_dataframe()

    def set_update(self, func):
        """Sets the callback function for the various parameters associated with this toolkit.

        :param func: - the callback function
        """
        self.starting.param.watch(func, "value")
        self.salary.param.watch(func, "value")
        self.salary_bonus.param.watch(func, "value")
        self.salary_cap.param.watch(func, "value")
        self.interest_rate.param.watch(func, "value")
        self.years.param.watch(func, "value")

    def update_dataframe(self):
        """Update method which sets the dataframe to updated values based on the values of the various inputs.
        """
        data_entries = []
        for i in range(self.years.value):
            cur_total, cur_base = growth(self.starting.value, i, self.salary.value, self.salary_bonus.value,
                               self.salary_cap.value, self.interest_rate.value)
            total_interest = cur_total - cur_base
            cur_salary = salary_growth(i, self.salary.value, self.salary_bonus.value, self.salary_cap.value)
            # ["total", "total_interest", "base", "salary", "year"]
            data_entries.append([cur_total, total_interest, cur_base, cur_salary, i])
        self.dataframe = pd.DataFrame(data_entries, columns=["total", "total_interest", "base", "income", "year"])

    def return_sidebar(self):
        """Return function to easily group the parameters to place in the sidebar of panel template.

        :return: - the parameters used for the toolkit
        """
        return [self.starting, self.salary, self.salary_bonus, self.salary_cap, self.interest_rate, self.years]

    def view_main(self):
        """Returns a graph showcasing the total growth of the portfolio over set amount of years.

        :return layout: - the panel column showing the respective graph data.
        """
        layout = pn.Column(
            self.dataframe.hvplot.bar(x="year", y="total"),
        )
        return layout

    def view_salary_info(self):
        """Returns a bar chart showcasing the growth of salary over time, and when it plateaus from the cap.

        :return layout: - the panel column showing the respective graph data.
        """
        layout = pn.Column(
            self.dataframe.hvplot.bar(x="year", y="income")
        )
        return layout

    def view_interest_info(self):
        """Returns a stacked barchart showcasing both pure interest gained as compared to base growth.

        :return layout: - the panel column showing the respective graph data.
        """
        layout = pn.Column(
            self.dataframe.hvplot.bar(stacked=True, x="year", y=["base", "total_interest"])
        )
        return layout

    def export_csv(self, filename):
        """Exports a csv file to specified directory

        :param filename: - filename to write the csv to.

        :return csv: - csv data which can be written out
        """
        return self.dataframe.to_csv(filename)
