class Roi():

    def init (self):
        pass


    def total_Income(self):
        print(" Please Enter Numbers only")
        rental_income = int(input("Enter Your Total Income monthly income: "))
        mis_income = int(input("Enter your Total miscellaneous Income: "))
        self.income = rental_income + mis_income
        print(f"Your total monthly income is : {self.income}")
           

    def total_expenses(self):
        
        print ( "Enter your Expenses:")
       
        tax = int(input("Enter Your expenses of Tax: "))
        insurance = int(input("Enter Your expenses of Insurances: "))
        print("Enter your Utilities expenses: ")
        electric = int(input("Electric: "))
        water = int(input("water: "))
        sewage = int(input("Sewage: "))
        garbage = int(input("Garbage: "))
        gas = int(input("Gas: "))
        hoa = int(input("Enter Your expenses of HOA Fees: "))
        loan = int(input("Enter Your expenses of Loan or snow maintainence: "))
        vacancy = int(input("Enter Your expenses of Vacancy: "))
        repairs = int(input("Enter Your expenses of repairs: "))
        capex = int(input("Enter Your expenses of Capital expenditures : "))
        prop = int(input("Enter Your expenses of Propertyy Management: "))
        mortgage = int(input("Enter Your expenses of Mortgage : "))
        self.expenses = tax + insurance + electric + water + sewage + garbage + gas + hoa + loan + vacancy + repairs + capex + prop + mortgage
        print (f"Your total Expenses are: {self.expenses} ")

    def cash_Flow(self):
        self.cash = self.income - self.expenses
        print (f"Your Cash Flow is {self.cash}month")
        self.annual_cash_flow = self.cash * 12
        print (f"Your  Annual Cash Flow is {self.annual_cash_flow}")

    def cash_on_cash(self):
        down_payment = int(input("Enter Your Down Payment : "))    
        closing_cost = int(input("Enter Your Closing Cost : ")) 
        rehab_budget = int(input("Enter Your Rehabilitation budget : ")) 
        mis = int(input("Enter Your any Miscellenous expense : "))  
        self.total_investment = down_payment + closing_cost + rehab_budget + mis
        print ( f"Your total investment is {self.total_investment}")
            
        self.roi = (self.annual_cash_flow/self.total_investment)  * 100
        print ( f"Your Return on Investment is {self.roi} ")


bigger_pockets = Roi()

def run():
    while True:
        print  ("Welcome to the Return on Investment Calculation(ROI)") 
        response = input(" Type 'Yes' to continue or 'quit' to leave  ")

        if response.lower() == 'yes':
            bigger_pockets.total_Income()
            bigger_pockets.total_expenses()
            bigger_pockets.cash_Flow()
            bigger_pockets.cash_on_cash()

        elif response.lower() == 'quit':    
            break
            

run()

