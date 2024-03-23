class Mortgage:
    def __init__(self, house, interestRate, loanTerm, downPayment):
        """
        downPayment can be either percentage or dollars. 
        If using percentage, downPayment < 1
        """
        if downPayment < 1:
            self.loanAmount = house.get_price() * (1 - downPayment)
            self.downPaymentAmount = house.get_price() * downPayment
            self.downPaymentPercent = downPayment
        else:
            self.loanAmount = house.get_price() - downPayment
            self.downPaymentAmount = downPayment
            self.downPaymentPercent = downPayment / house.get_price()
        self.interestRate = interestRate
        self.loanTerm = loanTerm
        self.monthlyPayment = round(self.calculate_monthly_payment(), 2)

    def calculate_monthly_payment(self):
        monthlyInterest = self.interestRate/12
        numberOfPayments = self.loanTerm*12
        return self.loanAmount*(monthlyInterest*(1+monthlyInterest)**numberOfPayments)/((1+monthlyInterest)**numberOfPayments-1)
    
    def print(self):
        print("Loan Amount: ${}\nInterest Rate {}%\nLoan Term: {} years\nDown Payment: ${} ({}%)\nMonthly Payment: ${}".format(self.loanAmount,
                                                                                                                                  self.interestRate*100,
                                                                                                                                  self.loanTerm,
                                                                                                                                  self.downPaymentAmount,
                                                                                                                                  self.downPaymentPercent*100,
                                                                                                                                  self.monthlyPayment))