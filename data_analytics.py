import panel as pn
import plotly.express as px
import pandas as pd


class DataAnalysis:
    def __init__(self):
        self.starting = pn.widgets.FloatInput(name="Starting funds", value=1000)
        self.salary = pn.widgets.FloatInput(name="Income")
        self.salary_bonus = pn.widgets.FloatInput(name="Bonus per year")
        self.salary_cap = pn.widgets.FloatInput(name="Income Ceiling")
        self.interest_rate = pn.widgets.FloatInput(name="Interest rate")
        self.years = pn.widgets.IntSlider(name="Years", start=0, end=100, value=0)
        self.dataframe = self.set_dataframe()

        self.starting.param.watch(self.update, "value")
        self.salary.param.watch(self.update, "value")
        self.salary_bonus.param.watch(self.update, "value")
        self.salary_cap.param.watch(self.update, "value")
        self.interest_rate.param.watch(self.update, "value")
        self.years.param.watch(self.update, "value")
        self.main_fig = None

    def update(self, event):
        self.update_dataframe()

    def update_dataframe(self):
        dic = {"Current Funds": self.starting.value, "Base Income": self.salary.value,
               "Yearly Bonus": self.salary_bonus.value, "Income Ceiling": self.salary_cap.value,
               "Interest Rate": self.interest_rate.value, "Year": self.years.value}
        self.dataframe = pd.concat([self.dataframe, pd.DataFrame([dic])], ignore_index=True)

    def set_dataframe(self):
        df = pd.DataFrame([[self.starting.value, self.salary.value, self.salary_bonus.value,
                          self.salary_cap.value, self.interest_rate.value, self.years.value]],
                          columns=["Current Funds", "Base Income", "Yearly Bonus",
                                   "Income Ceiling", "Interest Rate", "Year"])
        df.set_index("Year")
        return df

    def return_sidebar(self):
        return [self.starting, self.salary, self.salary_bonus, self.salary_cap, self.interest_rate, self.years]

    def salary_growth(self, years):
        salary = self.salary.value
        for i in range(years):
            if salary + self.salary_bonus.value < self.salary_cap.value:
                salary += self.salary_bonus.value
            else:
                return self.salary_cap.value
        return salary

    def growth(self, years, bonus=False, interest=False):
        base = self.starting.value
        total = self.starting.value
        salary = self.salary.value
        for i in range(years):
            total += salary
            base += salary
            if bonus:
                salary = self.salary_growth(i)
            if interest:
                total += total * self.interest_rate.value
        return [total, base]

    def view_main(self):
        self.main_fig = px.bar(self.dataframe, x="Year", y="Current Funds")
        return self.main_fig

    def view_salary_info(self):
        return "Test"

    def view_interest_info(self):
        return "Test"

    def print_report(self, years):
        total, base = self.growth(years, True, True)
        interest = total - base
        print("Generating report for the following conditions:"
              f"Starting amount: {self.starting.value}\n"
              f"Starting salary: {self.salary.value}\n"
              f"Salary increase per year: {self.salary_bonus.value}\n"
              f"Salary Cap: {self.salary_cap.value}\n"
              f"Interest per Year: {self.interest_rate.value}\n"
              f"Total Interest generated: {interest.value}\n"
              f"Total base saved: {base.value}\n"
              f"Total saved: {total.value}\n")
