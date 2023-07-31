import panel as pn

class DataAnalysis:
    def __init__(self):
        self.starting = pn.widgets.FloatInput(name="Starting funds")
        self.salary = pn.widgets.FloatInput(name="Income")
        self.salary_bonus = pn.widgets.FloatInput(name="Bonus per year")
        self.salary_cap = pn.widgets.FloatInput(name="Income Ceiling")
        self.interest_rate = pn.widgets.FloatInput(name="Interest rate")
        self.years = pn.widgets.IntSlider(name="Years", start=0, end=100, value=0)

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
