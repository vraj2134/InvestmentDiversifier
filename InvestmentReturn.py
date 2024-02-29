# class for calculating return on investment
class InvestmentReturn:

    def __init__(self):
        # private attribute for investment amount
        self.__investment_value = 0
        # private attribute for years of investment
        self.__investment_period = 0
        # private attribute for diversified percentages
        self.__div_percentage = []
        # private attribute for return on investment
        self.__return_on_investment = []
        # private attribute for declaring investment dictionary
        self.__dict = {0: "Equity",
                       1: "Debt",
                       2: "Crypto",
                       3: "Gold",
                       4: "Real Estate"
                       }
        self.menu()

    # menu method for calling the main menu
    def menu(self):

        while True:
            try:
                user_input = int(input("""
                Hello, How can we help you?
                1. Press 1 to provide your investment details.
                2. Press 2 to change your investment amount.
                3. Press 3 to change your holding period.
                4. Press 4 to change diversified percentages.
                5. Press 5 to calculate return on investment.
                6. Press any other key to exit.
                Please note : The rate of returns is as follows : 
                { Equity : 10%, Debt : 6.8%, Crypto : 670%, Gold : 10.8%, Real Estate : 10.6% } 
                """))

                if user_input in range(1, 7):
                    break
                else:
                    print("Please provide a valid number from the menu to continue.")
            except ValueError:
                print("Please provide a valid number from the menu to continue.")

        if user_input == 1:
            self.investment_detail()
        elif user_input == 2:
            self.change_amount()
        elif user_input == 3:
            self.change_period()
        elif user_input == 4:
            self.change_div_percentage()
        elif user_input == 5:
            self.calculate_roi()
        else:
            exit()

    # design is the static method for printing design
    def design(self):
        print("-*-"*34)

    # percentage method to take input of diversified percentage
    def percentage(self):
        try:
            input_string = input(
                "Please provide percentages of Equity, Debt, Crypto, Gold and Real Estate.(separated "
                "by spaces): ")
            percentages = list(map(float, input_string.split()))

            if len(percentages) < 5:
                for i in range(5-len(percentages)):
                    percentages.append(0)

            if any(num < 0 for num in percentages):
                print("Please provide positive percentage for these categories.")
                return self.percentage()
            elif sum(percentages) != 100:
                print("Please make sure that the sum of percentages is exactly 100.")
                return self.percentage()
            elif len(percentages) == 5 and sum(percentages) == 100:
                return percentages
            else:
                print("Please enter percentages only for these 5 categories.")
                return self.percentage()

        except ValueError:
            print("Please enter valid percentages separated by spaces.")
            return self.percentage()

    # investment_detail method takes input of investment amount, years of investment and diversified percentages
    def investment_detail(self):

        while True:
            try:
                amount = float(input("Please provide your amount of investment : $ "))
                if amount > 0:
                    break
                print("Please provide a positive numerical value for your amount of investment.")
            except ValueError:
                print("Please provide numerical value for your amount of investment.")

        self.__investment_value = amount

        while True:
            try:
                year = int(input("Please provide holding years of investment : "))
                if year > 0:
                    break
                print("Please provide a positive number for the years of investment.")
            except ValueError:
                print("Please provide number of years for the investment.")

        self.__investment_period = year

        self.__div_percentage = self.percentage()

        self.design()
        print("Investment amount is $", self.__investment_value, ".")
        print("Holding period of investment is", self.__investment_period, "years.")
        print("The investment will be ", self.__div_percentage[0], "% in equity,", self.__div_percentage[1],
              "% in debt,", self.__div_percentage[2], "% in crypto", self.__div_percentage[3], "% in gold, and",
              self.__div_percentage[4], "% in real estate.")
        print("Please note : 'Equity' investments will require a monthly contribution. Other categories are a one-time "
              "lumpsum investment.")
        self.design()
        self.menu()

    # change_amount method will change the investment amount
    def change_amount(self):
        if self.__investment_value > 0:
            while True:
                try:
                    new_amount = float(input("Please provide new amount of investment : $"))
                    if new_amount > 0:
                        self.__investment_value = new_amount
                        break
                    print("Please provide a positive numerical value for your amount of investment.")
                except ValueError:
                    print("Please provide a numerical value for your amount of investment.")

            self.design()
            print("New investment amount is $", self.__investment_value, ".")
            print("Holding period of investment is", self.__investment_period, "years.")
            print("The investment will be ", self.__div_percentage[0], "% in equity,", self.__div_percentage[1],
                  "% in debt,", self.__div_percentage[2], "% in crypto", self.__div_percentage[3], "% in gold, and",
                  self.__div_percentage[4], "% in real estate.")
            print("Please note : 'Equity' investments will require a monthly contribution. Other categories are a "
                  "one-time lumpsum investment.")
            self.design()
            self.menu()
        else:
            print("Please first provide the investment detail by pressing 1.")
            self.menu()

    # change_period method will change the investment years
    def change_period(self):
        if self.__investment_period > 0:
            while True:
                try:
                    new_period = int(input("Please provide holding years of investment : "))
                    if new_period > 0:
                        self.__investment_period = new_period
                        break
                    print("Please provide a positive number for the years of investment.")
                except ValueError:
                    print("Please provide number of years for the investment.")

            self.design()
            print("Investment amount is $", self.__investment_value, ".")
            print("New investment holding period is ", self.__investment_period, "years.")
            self.design()
            self.menu()
            print("The investment will be ", self.__div_percentage[0], "% in equity,", self.__div_percentage[1],
                  "% in debt,", self.__div_percentage[2], "% in crypto", self.__div_percentage[3], "% in gold, and",
                  self.__div_percentage[4], "% in real estate.")
            print("Please note : 'Equity' investments will require a monthly contribution. Other categories are a "
                  "one-time lumpsum investment.")
        else:
            print("Please provide the investment detail by pressing 1.")
            self.menu()

    # change_div_percentage method will change the diversified percentage
    def change_div_percentage(self):
        if self.__investment_value > 0 and self.__investment_period > 0:
            while True:
                try:
                    self.__div_percentage = self.percentage()
                    self.design()
                    print("Investment amount is $", self.__investment_value, ".")
                    print("New investment holding period is ", self.__investment_period, "years.")
                    print("The new investment will be ", self.__div_percentage[0], "% in equity,",
                          self.__div_percentage[1], "% in debt,", self.__div_percentage[2], "% in crypto",
                          self.__div_percentage[3], "% in gold, and", self.__div_percentage[4], "% in real estate.")
                    print("Please note : 'Equity' investments will require a monthly contribution. Other categories are"
                          " a one-time lumpsum investment.")
                    break
                except ValueError:
                    print("Please provide valid percentages.")
            self.design()
            self.menu()
        else:
            print("Please provide the investment detail by pressing 1.")
            self.menu()

    # comp_int is the static method for calculating future value of the investment considering compound interest
    def comp_int(self, p, r, t):
        amt = p
        for i in range(t):
            amt = amt * (1 + r / 100)
        return amt

    # calculate_roi method calculate return on investment for each category
    def calculate_roi(self):
        if self.__investment_value > 0 and self.__investment_period > 0:
            # diversified amount is the amount of investment for each category
            diversified_amount = [float(self.__investment_value * (i / 100)) for i in self.__div_percentage]
            # percentage CAGR of last 5 years of (equity,debt,crypto,gold,real estate)
            return_percentage = tuple(map(float, (10, 6.8, 670, 10.8, 10.6)))

            # location for output file given by the user
            # file_path = "D:/Industrial Engg DAL/Python/savings/Returns.txt"

            for i in range(5):
                # Code block under if is for calculating future value for 'Equity' investments only
                if i == 0:
                    p = diversified_amount[i]
                    r = return_percentage[i] / 12 / 100
                    n = 12 * self.__investment_period
                    roi = round(p * (1 + r) * ((1 + r) ** n - 1)/r, 2)

                    # below code block is for generating output values in the file located by user
                    # with open(file_path, "a") as file:
                    #     file.write(str(self.__dict[i]))
                    #     file.write(" is ")
                    #     file.write(str(roi))
                    #     file.write("\n")

                    self.design()
                    print("The final returns expected for", self.__dict[i], "is $", roi)

                else:
                    # this block calculate future values for Debt, Crypto, Gold and Real estate
                    roi = round(self.comp_int(diversified_amount[i], return_percentage[i], self.__investment_period), 2)
                    print("The final returns expected for", self.__dict[i], "is $", roi)
                self.__return_on_investment.append(roi)
            print("Total returns will be $", sum(self.__return_on_investment))
            self.design()
            self.menu()
        else:
            print("Please provide the investment detail by pressing 1.")
            self.menu()
            