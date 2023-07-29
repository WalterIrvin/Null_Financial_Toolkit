class DataAnalysis:
    def __init__(self, starting, salary, salary_bonus, salary_cap, interest):
        self.starting = starting
        self.salary = salary
        self.salary_bonus = salary_bonus
        self.salary_cap = salary_cap
        self.interest = interest

    def salary_growth(self, years):
        salary = self.salary
        for i in range(years):
            if salary + self.salary_bonus < self.salary_cap:
                salary += self.salary_bonus
            else:
                return self.salary_cap
        return salary

    def growth(self, years, bonus=False, interest=False):
        base = self.starting
        total = self.starting
        salary = self.salary
        for i in range(years):
            total += salary
            base += salary
            if bonus:
                salary = self.salary_growth(i)
            if interest:
                total += total * self.interest
        return [total, base]

    def print_report(self, years):
        total, base = self.growth(years, True, True)
        interest = total - base
        print("Generating report for the following conditions:"
              f"Starting amount: {self.starting}\n"
              f"Starting salary: {self.salary}\n"
              f"Salary increase per year: {self.salary_bonus}\n"
              f"Salary Cap: {self.salary_cap}\n"
              f"Interest per Year: {self.interest}\n"
              f"Total Interest generated: {interest}\n"
              f"Total base saved: {base}\n"
              f"Total saved: {total}\n")
