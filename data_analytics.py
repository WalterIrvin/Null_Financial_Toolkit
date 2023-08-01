import panel as pn
import pandas as pd
import hvplot.pandas


def salary_growth(years, income, bonus, cap):
    salary = income
    for i in range(years):
        if salary + bonus < cap:
            salary += bonus
        else:
            return cap
    return salary


def growth(starting, years, income=0, bonus=0, cap=0, interest=0):
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
        self.starting = pn.widgets.FloatInput(name="Starting funds")
        self.salary = pn.widgets.FloatInput(name="Income")
        self.salary_bonus = pn.widgets.FloatInput(name="Bonus per year")
        self.salary_cap = pn.widgets.FloatInput(name="Income Ceiling")
        self.interest_rate = pn.widgets.FloatInput(name="Interest rate")
        self.years = pn.widgets.IntInput(name="Years")
        self.dataframe = self.update_dataframe()
        self.main_fig = None

    def set_update(self, func):
        self.starting.param.watch(func, "value")
        self.salary.param.watch(func, "value")
        self.salary_bonus.param.watch(func, "value")
        self.salary_cap.param.watch(func, "value")
        self.interest_rate.param.watch(func, "value")
        self.years.param.watch(func, "value")

    def update_dataframe(self):
        data_entries = []
        for i in range(self.years.value):
            cur_total, cur_base = growth(self.starting.value, i, self.salary.value, self.salary_bonus.value,
                               self.salary_cap.value, self.interest_rate.value)
            total_interest = cur_total - cur_base
            cur_salary = salary_growth(i, self.salary.value, self.salary_bonus.value, self.salary_cap.value)
            # ["total", "total_interest", "base", "salary", "year"]
            data_entries.append([cur_total, total_interest, cur_base, cur_salary, i])
        df = pd.DataFrame(data_entries, columns=["total", "total_interest", "base", "income", "year"])
        print(df)
        return df

    def return_sidebar(self):
        return [self.starting, self.salary, self.salary_bonus, self.salary_cap, self.interest_rate, self.years]

    def view_main(self):
        layout = pn.Column(
            self.dataframe.hvplot.bar(x="year", y="total"),
        )
        return layout

    def view_salary_info(self):
        layout = pn.Column(
            self.dataframe.hvplot.bar(x="year", y="income")
        )
        return layout

    def view_interest_info(self):
        layout = pn.Column(
            self.dataframe.hvplot.bar(stacked=True, x="year", y=["base", "total_interest"])
        )
        return layout
