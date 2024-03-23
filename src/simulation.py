class Simulation:
    def __init__(self, mortgage, budget):
        self.mortgage = mortgage
        self.principal = mortgage.downPaymentAmount
        self.interest = 0
        self.loanBalance = mortgage.loanAmount
        self.budget = budget
        self.results = {"principal": [],
                        "interest": [],
                        "month": [],
                        "year": []}

    def amortization(self):
        principal = self.mortgage.monthlyPayment - (self.loanBalance*self.mortgage.interestRate/12)
        interest = self.mortgage.monthlyPayment - principal
        return round(principal, 2), round(interest, 2)

    def run(self):
        for i in range(self.mortgage.loanTerm*12):
            if self.loanBalance > 0:
                principal, interest = self.amortization()
                principal = round(principal + self.budget - self.mortgage.monthlyPayment)
            else:
                principal = 0
                interest = 0

            self.principal = round(self.principal + principal, 2)
            self.interest = round(self.interest + interest, 2)
            self.results["principal"].append(self.principal)
            self.results["interest"].append(self.interest)
            self.results["month"].append(i)
            self.results["year"].append(i/12)
            self.loanBalance = self.mortgage.loanAmount - self.principal